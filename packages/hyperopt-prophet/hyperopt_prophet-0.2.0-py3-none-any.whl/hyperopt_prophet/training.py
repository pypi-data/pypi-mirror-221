import json
import random
import warnings
from time import time

import mlflow
import mlflow.prophet
import pandas as pd
from hyperopt import hp
from mlflowops import MLFlowOps
from pydantic import BaseModel

from .model import ProphetHyperoptEstimator, mlflow_prophet_log_model, ProphetModel
from .utils import get_plotly_forecast, plotly_fig2pil

import logging

logging.getLogger("prophet").setLevel(logging.WARNING)
logging.getLogger("cmdstanpy").setLevel(logging.WARNING)


warnings.filterwarnings("ignore")


class ProphetTrainingParams(BaseModel):
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

    target_col: str = "y"
    time_col: str = "ds"
    unit: str = "minute"
    id_col: str = "ts_id"
    horizon: int = 1440
    interval_width: float = 0.8
    experiment_id: str = ""
    result_columns: list = [
        "ts_id",
        "run_id",
        "prophet_params",
        "start_time",
        "end_time",
        "training_duration",
        "mse",
        "rmse",
        "mae",
        "mape",
        "mdape",
        "smape",
        "coverage",
    ]
    result_schema: str = "struct<ts_id:string,run_id:string,prophet_params:string,start_time:timestamp,end_time:timestamp,training_duration:double,mse:double,rmse:double,mae:double,mape:double,mdape:double,smape:double,coverage:double>"
    loss_metric: str = "rmse"
    country_holidays: str = "US"
    num_folds: int = 2
    max_eval: int = 5
    trial_timeout: int = 6931
    is_parallel: bool = False
    random_state: int = random.randint(0, 9999)
    regressors: list = []
    prophet_kwargs: dict = {}
    include_forecast: bool = False
    base_model_name: str = ""
    search_space: dict = {
        "changepoint_prior_scale": hp.loguniform(
            "changepoint_prior_scale", -10.9, -0.69
        ),
        "seasonality_prior_scale": hp.loguniform("seasonality_prior_scale", -10.9, 5.3),
        "holidays_prior_scale": hp.loguniform("holidays_prior_scale", -10.9, 5.3),
        "seasonality_mode": hp.choice(
            "seasonality_mode", ["additive", "multiplicative"]
        ),
    }
    use_mlflow: bool = False

    class Config:
        env_file = "training.env"
        env_file_encoding = "utf-8"
        arbitrary_types_allowed = True
        extra = "ignore"


class ProphetHyperOptTrainer:
    def __init__(
        self, training_data: pd.DataFrame, training_params: ProphetTrainingParams
    ):
        self.training_data = training_data
        self.training_params = training_params
        self.ts_id = str(training_data[training_params.id_col].iloc[0])
        self.training_data["ds"] = pd.to_datetime(
            self.training_data[self.training_params.time_col]
        )
        self.training_data["y"] = self.training_data[self.training_params.target_col]

    def register_model(self, training_loss, training_run_id):
        runs_names = "prophet_" + self.ts_id
        mlops = MLFlowOps(
            runs_names=[runs_names],
            experiment_ids=self.training_params.experiment_id,
            base_model_name=self.training_params.base_model_name,
            sorting_metric=f"metrics.val_{self.training_params.loss_metric}",
            ascending=True,
        )
        mlops.check_model_improvement_and_transition_in_training_loop(
            training_loss, training_run_id
        )

    def training(self):
        # Set the start time of the run
        run_start_time = time()

        hyperopt_estim = ProphetHyperoptEstimator(
            horizon=self.training_params.horizon,
            frequency_unit=self.training_params.unit,
            metric=self.training_params.loss_metric,
            interval_width=self.training_params.interval_width,  # type: ignore
            country_holidays=self.training_params.country_holidays,
            search_space=self.training_params.search_space,
            num_folds=self.training_params.num_folds,
            max_eval=self.training_params.max_eval,
            trial_timeout=self.training_params.trial_timeout,
            is_parallel=self.training_params.is_parallel,
            random_state=self.training_params.random_state,
            # **{'uncertainty_samples': False}
            regressors=self.training_params.regressors,
            **self.training_params.prophet_kwargs,
        )

        result = hyperopt_estim.fit(self.training_data)
        result["ts_id"] = self.ts_id
        result["start_time"] = pd.Timestamp(
            self.training_data[self.training_params.time_col].min()
        )
        result["end_time"] = pd.Timestamp(
            self.training_data[self.training_params.time_col].max()
        )

        # Log the metrics to mlflow
        avg_metrics = (
            result[["mse", "rmse", "mae", "mape", "mdape", "smape", "coverage"]]
            .mean()
            .to_frame(name="mean_metrics")
            .reset_index()
        )
        avg_metrics["index"] = "val_" + avg_metrics["index"].astype(str)
        avg_metrics.set_index("index", inplace=True)

        # Create prophet model

        model_json = result["model_json"][0]

        prophet_model = ProphetModel(
            model_json=model_json,
            horizon=self.training_params.horizon,
            frequency=self.training_params.unit,
            time_col=self.training_params.time_col,
            regressors=self.training_params.regressors,
        )

        # prediction = prophet_model.predict_timeseries(
        #     horizon=self.training_params.horizon, include_history=True
        # )

        result["run_id"] = "local_training"

        # calculate the duration of the run in seconds
        result["training_duration"] = time() - run_start_time

        return prophet_model, model_json, result, avg_metrics  # , prediction

    def train_with_mlflow(self, mlflow_run):
        prophet_model, model_json, result, avg_metrics, prediction = self.training()

        # Generate sample input dataframe
        sample_input = self.training_data.head(20)
        sample_input[self.training_params.time_col] = pd.to_datetime(
            sample_input[self.training_params.time_col]
        )
        sample_input.drop(columns=["y"], inplace=True)

        model_dict = json.loads(model_json[list(model_json.keys())[0]])

        mlflow_prophet_log_model(prophet_model, sample_input=sample_input)

        for model_key in model_dict:
            if model_key not in [
                "changepoints",
                "history_dates",
                "train_holiday_names",
                "changepoints_t",
                "history",
                "train_component_cols",
                "params",
            ]:
                mlflow.log_param(model_key, model_dict[model_key])

        for key in self.training_params.dict():
            mlflow.log_param(key, self.training_params.dict()[key])

        mlflow.log_param("series_end_time", result["end_time"].iloc[0])
        mlflow.log_param("series_start_time", result["start_time"].iloc[0])
        mlflow.log_metrics(avg_metrics.to_dict()["mean_metrics"])

        id_model = prophet_model.model(self.ts_id)  # type: ignore

        fig = get_plotly_forecast(id_model, prediction)

        mlflow.log_image(image=plotly_fig2pil(fig), artifact_file="forecast.png")

        training_loss = result[self.training_params.loss_metric].iloc[0]
        training_run_id = mlflow_run.info.run_id

        result["run_id"] = training_run_id

        # get the start and end times for the run
        run_start_time = mlflow_run.info.start_time

        # calculate the duration of the run in seconds
        result["training_duration"] = round(time() * 1000) - run_start_time

        # Register the model
        self.register_model(
            training_loss=training_loss, training_run_id=training_run_id
        )

        return result[self.training_params.result_columns]

    def fit(self):
        if self.training_params.use_mlflow:
            with mlflow.start_run(
                experiment_id=self.training_params.experiment_id,
                run_name=f"prophet_{self.ts_id}",
            ) as mlflow_run:
                return self.train_with_mlflow(mlflow_run)
        else:
            return self.training()
