from environs import Env
from pydantic import BaseConfig

env = Env()


class Settings(BaseConfig):
    DB_HOST = env("DB_HOST")
    DATABASE = env("DATABASE")
    PORT = env("PORT")
    USERNAME = env("USERNAME")
    PASSWORD = env("PASSWORD")
    SCHEMA = env("SCHEMA")
    LOG_LEVEL = env.log_level("LOG_LEVEL")


SETTINGS = Settings
