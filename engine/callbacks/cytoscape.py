import json

import dash
from dash.dependencies import Input, Output, State

from app import dash_app, conn


@dash_app.callback(
    Output("cytoscape", "elements"),
    Input("cyto_interval", "n_intervals"),
    State("store_finished", "data")
)
def update_elements(n_interval, finished):
    if finished is None:
        return dash.no_update
    else:
        job_id = finished["id"]
        fetched = conn.get(job_id)

        if fetched is None:
            return dash.no_update

        job = json.loads(fetched.decode("utf-8"))
        result = job["result"]
        return result
