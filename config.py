import os
import dash_bootstrap_components as dbc


class Config:
    APP_NAME = "Graph_Viz_with_Dash_Cytoscape"
    BASE_DIR = os.path.dirname(__file__)
    DEBUG = False
    EXTERNAL_STYLESHEET = [dbc.themes.SPACELAB]
    PORT = 40147  # TODO: remove port
    PREVENT_INITIAL_CALLBACKS = True
    REDIS_URL = "localhost"
    SUPPRESS_CALLBACK_EXCEPTIONS = True
    URL_BASE_PATHNAME = "/"


class TestConfig(Config):
    DEBUG = True
