import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_cytoscape as cyto
import dash_html_components as html

from assets import styles

cyto.load_extra_layouts()


def get_search_panel():
    form = dbc.Form(
        [
            dbc.FormGroup(children=[dbc.Label("Github ID", className="mr-1"),
            dbc.Input(
                id="search_input_github_id", type="text", placeholder="Enter Github ID"
            )], className="mr-3"
                          )
            ,
            dbc.Button(
                "Search", id="search_button_search", color="primary", n_clicks=0)
        ],
        inline=True
    )

    status = dbc.Label("", id="search_status")
    return html.Div(
        children=[form, status], style={"margin-top": 10}
    )


def get_main_panel():
    status = html.Div("")

    cytoscape = cyto.Cytoscape(
        id="cytoscape",
        elements=[{"data": {"id": 0, "label": "Search github ID"}}],
        stylesheet=styles.get_cyto_stylesheet(),
        style={"height": "95vh", "width": "100%"},
        layout={"name": "cola", "nodeSpacing": 30},
    )

    return html.Div(
        children=[status, cytoscape], style={"margin-top": 10}
    )


def get_stores():
    submitted_store = dcc.Store(id="store_submitted", storage_type="memory")
    finished_store = dcc.Store(id="store_finished", storage_type="memory")
    status_interval = dcc.Interval(id="status_interval", interval=500)
    cyto_interval = dcc.Interval(id="cyto_interval", interval=500)
    return html.Div(
        children=[
            submitted_store,
            finished_store,
            status_interval,
            cyto_interval,
        ]
    )


def get_layout():
    search_panel = get_search_panel()
    main = get_main_panel()
    stores = get_stores()

    return html.Div(
        children=[
            stores,
            search_panel,
            main
        ]
    )
