import os
from .base import Config


class ProductionConfig(Config):
    DEBUG = False
    PORT = 40010
    REDIS_URL = os.getenv("REDISTOGO_URL", "redis://localhost:6379")
