from app import dash_app, app_config
from engine import callbacks

if __name__ == "__main__":
    dash_app.run_server(host="0.0.0.0", port=app_config.PORT, debug=app_config.DEBUG)
