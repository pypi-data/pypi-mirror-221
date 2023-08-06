from pydantic_settings import BaseSettings


def init():
    print("Hyperopt Prophet Utility Installed")


class HyperoptProphetSession(BaseSettings):
    ...

    class Config:
        env_file = ".env"
