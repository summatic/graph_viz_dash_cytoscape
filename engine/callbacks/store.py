import json

import dash
from dash.dependencies import Input, Output, State

from app import dash_app, conn, queue


@dash_app.callback(
    [
        Output("search_status", "children"),
        Output("store_finished", "data"),
        Output("cyto_interval", "disabled"),
        Output("search_button_search", "disabled")
    ],
    Input("status_interval", "n_intervals"),
    State("store_submitted", "data"),
)
def retrieve_status_output(n_interval, submitted):
    """Retrieve status output

    Refer to code snippet from "https://github.com/tcbegley/dash-rq-demo/blob/4cda74dc85da6f5dd5787723a09c85dd5d6103a2/
    dash_rq_demo/__init__.py#L73-L119"
    :param n_interval:
    :param submitted:
    :return:
    """
    if n_interval and submitted:
        job_id = submitted["id"]
        fetched = conn.get(job_id)

        if fetched is None:
            return dash.no_update, dash.no_update, dash.no_update

        job = json.loads(fetched.decode("utf-8"))

        status = job["status"]

        if status in ["finished", "no_input", "not_found"]:
            return status, {"id": submitted["id"]}, False, False
        if status == "wait":
            order = job["order"]
            return f"{order} jobs were queued.", None, True, True
        else:
            return status, None, True, True
    else:
        return dash.no_update, None, True, False


@dash_app.callback(
    Output("status_interval", "disabled"),
    [Input("store_submitted", "data"), Input("store_finished", "data")]
)
def disable_status_interval(submitted, finished):
    """Disable interval

    Refer to code snippet from "https://github.com/tcbegley/dash-rq-demo/blob/4cda74dc85da6f5dd5787723a09c85dd5d6103a2/
    dash_rq_demo/__init__.py#L122-L134"
    """
    if submitted:
        if finished and submitted["id"] == finished["id"]:
            # most recently submitted job has finished, no need for interval
            return True
        # most recent job has not yet finished, keep interval going
        return False
    # no jobs submitted yet, disable interval
    return True
