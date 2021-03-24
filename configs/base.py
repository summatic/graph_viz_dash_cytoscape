import os
import dash_bootstrap_components as dbc


class Config:
    APP_NAME = "Graph_Viz_with_Dash_Cytoscape"
    BASE_DIR = os.path.dirname(__file__)
    EXTERNAL_STYLESHEET = [dbc.themes.SPACELAB]
    PREVENT_INITIAL_CALLBACKS = True
    PORT = os.getenv("PORT")
    SUPPRESS_CALLBACK_EXCEPTIONS = True
    URL_BASE_PATHNAME = "/"
