import dash
import os
import redis
from flask import Flask

from assets import layout
from configs import DevConfig, TestConfig, ProductionConfig
from engine.redis_queue import RQueue


def init_dash(server, config):
    return dash.Dash(
        name=config.APP_NAME,
        server=server,
        url_base_pathname=config.URL_BASE_PATHNAME,
        external_stylesheets=config.EXTERNAL_STYLESHEET,
        suppress_callback_exceptions=config.SUPPRESS_CALLBACK_EXCEPTIONS,
        prevent_initial_callbacks=config.PREVENT_INITIAL_CALLBACKS,
        title=config.APP_NAME,
    )


def init_rq(server, config):
    redis_url = config.REDIS_URL
    conn = redis.from_url(url=redis_url)
    rq = RQueue(name="default", conn=conn)

    return rq, conn


def init_app(config):
    """Construct core Flask application with embedded Dash app."""
    server = Flask(
        __name__, instance_relative_config=False, template_folder="templates"
    )

    _dash_app = init_dash(server, config)
    _rq, _conn = init_rq(server, config)

    with server.app_context():
        return {"dash_app": _dash_app, "rq": _rq, "conn": _conn}


mode = os.environ["DASH_MODE"]
if mode == "dev":
    app_config = DevConfig
elif mode == "test":
    app_config = TestConfig
elif mode == "production":
    app_config = ProductionConfig
else:
    raise ValueError("Choose mode")

init = init_app(config=app_config)
dash_app = init["dash_app"]
queue = init["rq"]
conn = init["conn"]
dash_app.layout = layout.get_layout()
