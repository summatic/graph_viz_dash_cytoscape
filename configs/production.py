import os
from .base import Config


class ProductionConfig(Config):
    DEBUG = False
    REDIS_URL = os.getenv("REDISTOGO_URL", "redis://localhost:6379")
