import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            body {
                font-size: 0.9rem;  /* smaller than Bootstrap default */
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""


app.layout = dbc.Container(
    fluid=True,
    children=[
        # ===================== Project Header =====================
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5("Project setup"),

                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Label("Project name"),
                                        dbc.Input(
                                            id="project-name",
                                            type="text",
                                            placeholder="Enter project name",
                                        ),
                                    ],
                                    md=6,
                                ),
                                dbc.Col(
                                    [
                                        dbc.Label("Project status"),
                                        html.Div(
                                            id="project-status",
                                            children="No project loaded",
                                            className="text-muted",
                                        ),
                                    ],
                                    md=6,
                                    className="d-flex flex-column justify-content-end",
                                ),
                            ],
                            className="mb-2",
                        ),

                        dbc.ButtonGroup(
                            [
                                dbc.Button("New", id="btn-new-project", color="secondary"),
                                dbc.Button("Open", id="btn-open-project", color="secondary"),
                                dbc.Button("Save", id="btn-save-project", color="primary",disabled=True),
                                dbc.Button("Save As", id="btn-save-as-project", color="secondary",disabled=True),
                            ],
                            className="mb-3",
                        ),
                    ],
                    width=12,
                )
            ],
            className="mt-3",
        ),

        html.Hr(),

        # ===================== Data Sources Section =====================
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H6("Data sources"),

                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Button(
                                        "Add source",
                                        id="btn-add-source",
                                        disabled=True,
                                        color="primary",
                                        className="me-2",
                                    ),
                                    width="auto",
                                ),
                                dbc.Col(
                                    dbc.Button(
                                        "Refresh sources",
                                        id="btn-refresh-sources",
                                        disabled=True,
                                        color="secondary",
                                    ),
                                    width="auto",
                                ),
                            ],
                            className="mb-3",
                        ),

                        # Table / list placeholder for data sources
                        dbc.Table(
                            id="tbl-data-sources",
                            bordered=True,
                            hover=True,
                            striped=True,
                            className="mb-3",
                        ),

                        # Modal for adding / editing a data source
                        dbc.Modal(
                            id="modal-add-source",
                            is_open=False,
                            children=[
                                dbc.ModalHeader(dbc.ModalTitle("Add data source")),
                                dbc.ModalBody(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        dbc.Label("Source type"),
                                                        dcc.Dropdown(
                                                            id="input-source-type",
                                                            options=[
                                                                {
                                                                    "label": "URL",
                                                                    "value": "url",
                                                                },
                                                                {
                                                                    "label": "Server file",
                                                                    "value": "server_file",
                                                                },
                                                                {
                                                                    "label": "Server directory",
                                                                    "value": "server_directory",
                                                                },
                                                                {
                                                                    "label": "Uploaded file",
                                                                    "value": "uploaded",
                                                                },
                                                            ],
                                                            placeholder="Select source type",
                                                        ),
                                                    ],
                                                    className="mb-3",
                                                )
                                            ]
                                        ),
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        dbc.Label("Value"),
                                                        # NOTE: behavior will depend on type:
                                                        # - url/server_*: text input
                                                        # - uploaded: dcc.Upload
                                                        # For now we keep simple text; you can
                                                        # later swap it based on type via callbacks.
                                                        dbc.Input(
                                                            id="input-source-value",
                                                            type="text",
                                                            placeholder="Enter URL, path or description",
                                                        ),
                                                    ]
                                                )
                                            ]
                                        ),
                                    ]
                                ),
                                dbc.ModalFooter(
                                    [
                                        dbc.Button(
                                            "Cancel",
                                            id="btn-cancel-add-source",
                                            color="secondary",
                                            className="me-2",
                                        ),
                                        dbc.Button(
                                            "Add",
                                            id="btn-confirm-add-source",
                                            color="primary",
                                        ),
                                    ]
                                ),
                            ],
                        ),
                    ],
                    width=12,
                )
            ]
        ),

        html.Hr(),

        # ===================== Demographics & Analysis Definitions =====================
        dbc.Row(
            [
                # Demographics
                dbc.Col(
                    [
                        html.H6("Demographics file"),

                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Label("Type"),
                                        dcc.Dropdown(
                                            id="demographics-type",
                                            options=[
                                                {
                                                    "label": "Server file",
                                                    "value": "server_file",
                                                },
                                                {
                                                    "label": "Uploaded file",
                                                    "value": "uploaded",
                                                },
                                            ],
                                            placeholder="Select file type",
                                        ),
                                    ],
                                    className="mb-3",
                                )
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Label("Value"),
                                        # For MVP: keep as text; later you can show
                                        # dcc.Upload when type == uploaded.
                                        dbc.Input(
                                            id="demographics-value",
                                            type="text",
                                            placeholder="Path or identifier",
                                        ),
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            id="demographics-status",
                            className="mt-2 text-muted",
                            children="No demographics file selected",
                        ),
                    ],
                    md=6,
                ),

                # Analysis definitions
                dbc.Col(
                    [
                        html.H6("Analysis definitions"),

                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Label("Type"),
                                        dcc.Dropdown(
                                            id="analysis-def-type",
                                            options=[
                                                {
                                                    "label": "Server file",
                                                    "value": "server_file",
                                                },
                                                {
                                                    "label": "Uploaded file",
                                                    "value": "uploaded",
                                                },
                                            ],
                                            placeholder="Select file type",
                                        ),
                                    ],
                                    className="mb-3",
                                )
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Label("Value"),
                                        dbc.Input(
                                            id="analysis-def-value",
                                            type="text",
                                            placeholder="Path or identifier",
                                        ),
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            id="analysis-def-status",
                            className="mt-2 text-muted",
                            children="No analysis definitions file selected",
                        ),
                    ],
                    md=6,
                ),
            ],
            className="mt-4",
        ),

        html.Hr(),

        # ===================== Selections =====================
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H6("Selections"),

                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Label("Territories"),
                                        dcc.Dropdown(
                                            id="select-territories",
                                            options=[],  # to be filled by callbacks
                                            multi=True,
                                            placeholder="Select territories",
                                        ),
                                    ],
                                    md=6,
                                ),
                                dbc.Col(
                                    [
                                        dbc.Label("Source files"),
                                        dcc.Dropdown(
                                            id="select-source-files",
                                            options=[],  # to be filled by callbacks
                                            multi=True,
                                            placeholder="Select source files",
                                        ),
                                    ],
                                    md=6,
                                ),
                            ],
                            className="mb-3",
                        ),

                        dbc.Button(
                            "Clear selections",
                            id="btn-clear-selections",
                            color="secondary",
                            size="sm",
                            className="mb-3",
                        ),

                        html.Div(
                            id="selections-status",
                            className="text-muted",
                            children="No territories or source files selected",
                        ),
                    ],
                    width=12,
                )
            ],
            className="mt-4",
        ),

        html.Hr(),

        # ===================== Footer =====================
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.ButtonGroup(
                            [
                                dbc.Button(
                                    "Save",
                                    id="footer-btn-save",
                                    color="primary",
                                ),
                                dbc.Button(
                                    "Save As",
                                    id="footer-btn-save-as",
                                    color="secondary",
                                ),
                                dbc.Button(
                                    "Continue to analysis",
                                    id="btn-continue-analysis",
                                    color="success",
                                    disabled=True,  # enabled by validation later
                                ),
                            ]
                        ),
                        html.Div(
                            id="validation-messages",
                            className="mt-2 text-danger",
                        ),
                    ],
                    width=12,
                )
            ],
            className="mb-4",
        ),

        # ===================== Hidden stores for state (for future callbacks) =====================
        dcc.Store(id="store-project-json"),
        dcc.Store(id="store-data-sources"),
        dcc.Store(id="store-validation-state"),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
