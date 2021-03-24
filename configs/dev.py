import os
from .base import Config


class DevConfig(Config):
    DEBUG = False
    REDIS_URL = "redis://localhost:6379"


class TestConfig(DevConfig):
    DEBUG = True
