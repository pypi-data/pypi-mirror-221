import logging
from abc import ABC, abstractmethod
from enum import Enum
from functools import partial
from typing import Any, Dict, List, Optional, Union, Tuple

import cloudpickle
import hyperopt
import mlflow
import numpy as np
import pandas as pd
import prophet
from hyperopt import SparkTrials, Trials, fmin
from mlflow.exceptions import MlflowException
from mlflow.models.signature import ModelSignature, infer_signature
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE
from mlflow.utils.environment import _mlflow_conda_env
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
from prophet.serialize import model_to_json

from .utils import (
    DATE_OFFSET_KEYWORD_MAP,
    OFFSET_ALIAS_MAP,
    generate_cutoffs,
    get_validation_horizon,
    is_quaterly_alias,
)

import logging
logger = logging.getLogger('cmdstanpy')
logger.addHandler(logging.NullHandler())
logger.propagate = False
logger.setLevel(logging.CRITICAL)

class ForecastModel(ABC, mlflow.pyfunc.PythonModel):
    @abstractmethod
    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def model_env(self):
        pass  # pragma: no cover

    @staticmethod
    def _validate_cols(df: pd.DataFrame, required_cols: List[str]):
        df_cols = set(df.columns)
        required_cols_set = set(required_cols)
        if not required_cols_set.issubset(df_cols):
            raise MlflowException(
                message=(
                    f"Input data columns '{list(df_cols)}' do not contain the required columns '{required_cols}'"
                ),
                error_code=INVALID_PARAMETER_VALUE,
            )

    def infer_signature(self, sample_input: pd.DataFrame = None) -> ModelSignature:  # type: ignore
        signature = infer_signature(
            sample_input, self.predict(context=None, model_input=sample_input)
        )
        return signature


def mlflow_forecast_log_model(
    forecast_model: ForecastModel, sample_input: pd.DataFrame = None
) -> None:  # type: ignore
    """
    Log the model to mlflow
    :param forecast_model: Forecast model wrapper
    :param sample_input: sample input Dataframes for model inference
    """
    # log the model without signature if infer_signature is failed.
    try:
        signature = forecast_model.infer_signature(sample_input)
    except Exception:  # noqa
        signature = None
    mlflow.pyfunc.log_model(
        "model",
        conda_env=forecast_model.model_env,
        python_model=forecast_model,
        signature=signature,
    )  # type: ignore


PROPHET_CONDA_ENV = _mlflow_conda_env(
    additional_pip_deps=[
        f"prophet=={prophet.__version__}",
        f"cloudpickle=={cloudpickle.__version__}",
    ]
)


class ProphetModel(ForecastModel):
    """
    Prophet mlflow model wrapper for univariate forecasting.
    """

    def __init__(
        self,
        model_json: Union[Dict[Tuple, str], str],
        horizon: int,
        frequency: str,
        time_col: str,
        regressors: List[str] = None,
    ) -> None:
        """
        Initialize the mlflow Python model wrapper for mlflow
        :param model_json: json string of the Prophet model or
        the dictionary of json strings of Prophet model for multi-series forecasting
        :param horizon: Int number of periods to forecast forward.
        :param frequency: the frequency of the time series
        :param time_col: the column name of the time column
        """
        self._model_json = model_json
        self._horizon = horizon
        self._frequency = frequency
        self._time_col = time_col
        self._is_quaterly = is_quaterly_alias(frequency)
        self.regressors = regressors or []
        super().__init__()

    def load_context(self, context: mlflow.pyfunc.model.PythonModelContext) -> None:
        """
        Loads artifacts from the specified :class:`~PythonModelContext` that can be used
        :param context: A :class:`~PythonModelContext` instance containing artifacts that the model
                        can use to perform inference.
        """
        from prophet import Prophet  # noqa: F401

        return

    @property
    def model_env(self):
        return PROPHET_CONDA_ENV

    def model(self) -> prophet.forecaster.Prophet:
        """
        Deserialize a Prophet model from json string
        :return: Prophet model
        """
        from prophet.serialize import model_from_json

        return model_from_json(self._model_json)

    def make_future_dataframe(
        self, horizon: int = None, include_history: bool = True
    ) -> pd.DataFrame:
        """
        Generate future dataframe by calling the API from prophet
        :param horizon: Int number of periods to forecast forward.
        :param include_history: Boolean to include the historical dates in the data
            frame for predictions.
        :return: pd.Dataframe that extends forward from the end of self.history for the
        requested number of periods.
        """
        offset_kwarg = DATE_OFFSET_KEYWORD_MAP[OFFSET_ALIAS_MAP[self._frequency]]

        futures = self.model().make_future_dataframe(
            periods=horizon or self._horizon,
            freq=pd.DateOffset(**offset_kwarg),
            include_history=include_history,
        )
        # Create a new DataFrame with the original columns and the new columns
        new_df = pd.DataFrame(columns=futures.columns.tolist() + self.regressors)

        # Copy the original DataFrame to the new DataFrame
        new_df[futures.columns] = futures
        new_df.fillna(0, inplace=True)
        return new_df
        # futures = self.add_regressor_to_future(future, [temp, rain, sun, wind])

    def _predict_impl(
        self, horizon: int = None, include_history: bool = True
    ) -> pd.DataFrame:
        """
        Predict using the API from prophet model.
        :param horizon: Int number of periods to forecast forward.
        :param include_history: Boolean to include the historical dates in the data
            frame for predictions.
        :return: A pd.DataFrame with the forecast components.
        """
        future_pd = self.make_future_dataframe(
            horizon=horizon or self._horizon, include_history=include_history
        )
        return self.model().predict(future_pd)

    def predict_timeseries(
        self, horizon: int = None, include_history: bool = True
    ) -> pd.DataFrame:
        """
        Predict using the prophet model.
        :param horizon: Int number of periods to forecast forward.
        :param include_history: Boolean to include the historical dates in the data
            frame for predictions.
        :return: A pd.DataFrame with the forecast components.
        """
        return self._predict_impl(horizon, include_history)

    def predict(
        self, context: mlflow.pyfunc.model.PythonModelContext, model_input: pd.DataFrame
    ) -> pd.Series:
        """
        Predict API from mlflow.pyfunc.PythonModel
        :param context: A :class:`~PythonModelContext` instance containing artifacts that the model
                        can use to perform inference.
        :param model_input: Input dataframe
        :return: A pd.DataFrame with the forecast components.
        """
        self._validate_cols(model_input, [self._time_col])
        test_df = pd.DataFrame({"ds": model_input[self._time_col]})
        predict_df = self.model().predict(test_df)
        return predict_df["yhat"]

    def infer_signature(self, sample_input: pd.DataFrame = None) -> ModelSignature:
        if sample_input is None:
            sample_input = self.make_future_dataframe(horizon=1)
            sample_input.rename(columns={"ds": self._time_col}, inplace=True)
        return super().infer_signature(sample_input)


def mlflow_prophet_log_model(
    prophet_model: ProphetModel,
    sample_input: pd.DataFrame = None,
) -> None:  # type: ignore
    """
    Log the model to mlflow
    :param prophet_model: Prophet model wrapper
    :param sample_input: sample input Dataframes for model inference
    """
    mlflow_forecast_log_model(prophet_model, sample_input)


class ProphetHyperParams(Enum):
    CHANGEPOINT_PRIOR_SCALE = "changepoint_prior_scale"
    SEASONALITY_PRIOR_SCALE = "seasonality_prior_scale"
    HOLIDAYS_PRIOR_SCALE = "holidays_prior_scale"
    SEASONALITY_MODE = "seasonality_mode"


def _prophet_fit_predict(
    params: Dict[str, Any],
    history_pd: pd.DataFrame,
    horizon: int,
    frequency: str,
    cutoffs: List[pd.Timestamp],
    interval_width: int,
    primary_metric: str,
    country_holidays: Optional[str] = None,
    regressors=None,
    **prophet_kwargs,
) -> Dict[str, Any]:
    """
    Training function for hyperparameter tuning with hyperopt

    :param params: Input hyperparameters
    :param history_pd: pd.DataFrame containing the history. Must have columns ds (date
            type) and y, the time series
    :param horizon: Forecast horizon_timedelta
    :param frequency: Frequency of the time series
    :param num_folds: Number of folds for cross validation
    :param interval_width: Width of the uncertainty intervals provided for the forecast
    :param primary_metric: Metric that will be optimized across trials
    :param country_holidays: Built-in holidays for the specified country
    :param prophet_kwargs: Optional keyword arguments for Prophet model.
    :return: Dictionary as the format for hyperopt
    """
    input_params = {**params, **prophet_kwargs}
    model = Prophet(interval_width=interval_width, **input_params)
    if country_holidays:
        model.add_country_holidays(country_name=country_holidays)

    if regressors:
        for regressor in regressors:
            model.add_regressor(regressor)

    model.fit(history_pd, iter=200)
    # offset_kwarg = DATE_OFFSET_KEYWORD_MAP[OFFSET_ALIAS_MAP[frequency]]
    # horizon_offset = pd.DateOffset(**offset_kwarg) * horizon
    horizon_timedelta = pd.to_timedelta(horizon, unit=frequency)
    # Evaluate Metrics
    df_cv = cross_validation(
        model, horizon=horizon_timedelta, cutoffs=cutoffs, disable_tqdm=True
    )  # disable tqdm to make it work with ipykernel and reduce the output size
    df_metrics = performance_metrics(df_cv)

    metrics = df_metrics.mean().drop("horizon").to_dict()

    return {
        "loss": metrics[primary_metric],
        "metrics": metrics,
        "status": hyperopt.STATUS_OK,
    }


class ProphetHyperoptEstimator(ABC):
    """
    Class to do hyper-parameter tunings for prophet with hyperopt
    """

    SUPPORTED_METRICS = ["mse", "rmse", "mae", "mape", "mdape", "smape", "coverage"]

    def __init__(
        self,
        horizon: int,
        frequency_unit: str,
        metric: str,
        interval_width: int,
        country_holidays: str,
        search_space: Dict[str, Any],
        algo=hyperopt.tpe.suggest,
        num_folds: int = 5,
        max_eval: int = 10,
        trial_timeout: int = None,
        random_state: int = 0,
        is_parallel: bool = True,
        regressors=None,
        **prophet_kwargs,
    ) -> None:
        """
        Initialization

        :param horizon: Number of periods to forecast forward
        :param frequency_unit: Frequency of the time series
        :param metric: Metric that will be optimized across trials
        :param interval_width: Width of the uncertainty intervals provided for the forecast
        :param country_holidays: Built-in holidays for the specified country
        :param search_space: Search space for hyperparameter tuning with hyperopt
        :param algo: Search algorithm
        :param num_folds: Number of folds for cross validation
        :param max_eval: Max number of trials generated in hyperopt
        :param trial_timeout: timeout for hyperopt
        :param random_state: random seed for hyperopt
        :param is_parallel: Indicators to decide that whether run hyperopt in
        :param regressors: list of column names of external regressors
        :param prophet_kwargs: Optional keyword arguments for Prophet model.
            For information about the parameters see:
            `The Prophet source code <https://github.com/facebook/prophet/blob/master/python/prophet/forecaster.py>`_.
        """
        self._horizon = horizon
        self._frequency_unit = OFFSET_ALIAS_MAP[frequency_unit]
        self._metric = metric
        self._interval_width = interval_width
        self._country_holidays = country_holidays
        self._search_space = search_space
        self._algo = algo
        self._num_folds = num_folds
        self._random_state = np.random.default_rng(random_state)
        self._max_eval = max_eval
        self._timeout = trial_timeout
        self._is_parallel = is_parallel
        self._regressors = regressors
        self._prophet_kwargs = prophet_kwargs

    def fit(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Fit the Prophet model with hyperparameter tunings
        :param df: pd.DataFrame containing the history. Must have columns ds (date
            type) and y
        :return: DataFrame with model json and metrics in cross validation
        """
        df["ds"] = pd.to_datetime(df["ds"])

        seasonality_mode = ["additive", "multiplicative"]

        validation_horizon = get_validation_horizon(
            df, self._horizon, self._frequency_unit
        )
        cutoffs = generate_cutoffs(
            df.reset_index(drop=True),
            horizon=validation_horizon,
            unit=self._frequency_unit,
            num_folds=self._num_folds,
        )

        train_fn = partial(
            _prophet_fit_predict,
            history_pd=df,
            horizon=validation_horizon,
            frequency=self._frequency_unit,
            cutoffs=cutoffs,
            interval_width=self._interval_width,
            primary_metric=self._metric,
            country_holidays=self._country_holidays,
            regressors=self._regressors,
            **self._prophet_kwargs,
        )

        if self._is_parallel:
            trials = SparkTrials()  # pragma: no cover
        else:
            trials = Trials()

        best_result = fmin(
            fn=train_fn,
            space=self._search_space,
            algo=self._algo,
            max_evals=self._max_eval,
            trials=trials,
            timeout=self._timeout,
            rstate=self._random_state,
        )

        # Retrain the model with all history data.
        model = Prophet(
            changepoint_prior_scale=best_result.get(
                ProphetHyperParams.CHANGEPOINT_PRIOR_SCALE.value, 0.05
            ),
            seasonality_prior_scale=best_result.get(
                ProphetHyperParams.SEASONALITY_PRIOR_SCALE.value, 10.0
            ),
            holidays_prior_scale=best_result.get(
                ProphetHyperParams.HOLIDAYS_PRIOR_SCALE.value, 10.0
            ),
            seasonality_mode=seasonality_mode[
                best_result.get(ProphetHyperParams.SEASONALITY_MODE.value, 0)
            ],
            interval_width=self._interval_width,
            **self._prophet_kwargs,
        )

        if self._country_holidays:
            model.add_country_holidays(country_name=self._country_holidays)

        if self._regressors:
            for regressor in self._regressors:
                model.add_regressor(regressor)

        model.fit(df)

        model_json = model_to_json(model)
        metrics = trials.best_trial["result"]["metrics"]

        results_pd = pd.DataFrame({"model_json": model_json}, index=[0])
        results_pd.reset_index(level=0, inplace=True)
        for metric in self.SUPPORTED_METRICS:
            if metric in metrics.keys():
                results_pd[metric] = metrics[metric]
            else:
                results_pd[metric] = np.nan
        results_pd["prophet_params"] = str(best_result)

        return results_pd
