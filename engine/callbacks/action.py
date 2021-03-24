import uuid
import json

from dash.dependencies import Input, Output, State

from app import dash_app, queue, conn


@dash_app.callback(
    Output("store_submitted", "data"),
    Input("search_button_search", "n_clicks"),
    State("search_input_github_id", "value")
)
def submit_job(n_clicks, github_id):
    if github_id is None:
        github_id = ""

    if n_clicks > 0:
        job_id = str(uuid.uuid4())
        element = json.dumps({"job_id": job_id, "github_id": github_id})
        queue.put(element)
        conn.set(name=job_id, value=json.dumps({"status": "wait", "result": None, "order": queue.size}))

        return {"id": job_id}
    else:
        return {}
