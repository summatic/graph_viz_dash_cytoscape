import dash
import redis
from flask import Flask
from engine.redis_queue import RQueue

from assets import layout
from config import Config, TestConfig


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
    conn = redis.Redis(host=redis_url, port=6379)
    rq = RQueue(name="defalut", conn=conn)

    # w = Worker([rq], connection=conn)
    # w.work()
    return rq, conn


def init_app(config):
    """Construct core Flask application with embedded Dash app."""
    server = Flask(__name__, instance_relative_config=False, template_folder="templates")

    _dash_app = init_dash(server, config)
    _rq, _conn = init_rq(server, config)

    with server.app_context():
        # return {"dash_app": _dash_app}
        return {"dash_app": _dash_app, "rq": _rq, "conn": _conn}


# mode = os.environ["DASH_MODE"]
mode = "test"
if mode == "dev":
    app_config = Config
elif mode == "test":
    app_config = TestConfig
else:
    raise ValueError("Choose mode")

init = init_app(config=app_config)
dash_app = init["dash_app"]
queue = init["rq"]
conn = init["conn"]
dash_app.layout = layout.get_layout()
