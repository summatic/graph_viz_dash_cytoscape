import os
from .base import Config


class DevConfig(Config):
    DEBUG = False
    PORT = os.getenv("DASH_PORT")
    REDIS_URL = "redis://localhost:6379"


class TestConfig(DevConfig):
    DEBUG = True
