import dash_bootstrap_components as dbc
from dash import html, dcc

add_source_modal = dbc.Modal(
    [
        dbc.ModalHeader("Add Data Source"),
        dbc.ModalBody(
            dbc.Tabs(
                [
                    dbc.Tab(
                        dcc.Upload(
                            id="upload-local-source",
                            children=html.Div("Drag & drop or click to upload"),
                            multiple=False
                        ),
                        label="Local File"
                    ),
                    dbc.Tab(
                        dbc.Input(
                            id="input-url-source",
                            type="text",
                            placeholder="Enter URL"
                        ),
                        label="URL"
                    ),
                    dbc.Tab(
                        dcc.Dropdown(
                            id="dropdown-server-source",
                            options=[],
                            placeholder="Select server file"
                        ),
                        label="Server Directory"
                    ),
                ]
            )
        ),
        dbc.ModalFooter(
            [
                dbc.Button("Add", id="btn-confirm-add-source"),
                dbc.Button("Cancel", id="btn-cancel-add-source"),
            ]
        )
    ],
    id="modal-add-source",
    is_open=False
)

demographics_modal = dbc.Modal(
    [
        dbc.ModalHeader("Select Demographics File"),
        dbc.ModalBody(
            dbc.Tabs(
                [
                    dbc.Tab(
                        [
                            html.Div("Upload a local demographics file", className="mb-2"),
                            dcc.Upload(
                                id="upload-demographics-local",
                                children=html.Div("Drag & drop or click to upload"),
                                multiple=False,
                                className="border p-3 text-center"
                            ),
                        ],
                        label="Local File",
                    ),
                    dbc.Tab(
                        [
                            html.Div("Enter a URL to a demographics file", className="mb-2"),
                            dbc.Input(
                                id="input-demographics-url",
                                type="text",
                                placeholder="https://example.com/demographics.csv",
                            ),
                        ],
                        label="URL",
                    ),
                    dbc.Tab(
                        [
                            html.Div("Select a server-side demographics file", className="mb-2"),
                            dcc.Dropdown(
                                id="dropdown-demographics-server",
                                options=[],
                                placeholder="Choose a file",
                            ),
                        ],
                        label="Server Directory",
                    ),
                ]
            )
        ),
        dbc.ModalFooter(
            [
                dbc.Button("Apply", id="btn-confirm-demographics", color="primary"),
                dbc.Button("Cancel", id="btn-cancel-demographics", color="secondary"),
            ]
        ),
    ],
    id="modal-demographics",
    is_open=False,
    size="lg",
)

analysis_modal = dbc.Modal(
    [
        dbc.ModalHeader("Select Analysis Definitions"),
        dbc.ModalBody(
            dbc.Tabs(
                [
                    dbc.Tab(
                        [
                            html.Div("Upload a local analysis definitions file", className="mb-2"),
                            dcc.Upload(
                                id="upload-analysis-local",
                                children=html.Div("Drag & drop or click to upload"),
                                multiple=False,
                                className="border p-3 text-center"
                            ),
                        ],
                        label="Local File",
                    ),
                    dbc.Tab(
                        [
                            html.Div("Enter a URL to an analysis definitions file", className="mb-2"),
                            dbc.Input(
                                id="input-analysis-url",
                                type="text",
                                placeholder="https://example.com/analysis.json",
                            ),
                        ],
                        label="URL",
                    ),
                    dbc.Tab(
                        [
                            html.Div("Select a server-side analysis file", className="mb-2"),
                            dcc.Dropdown(
                                id="dropdown-analysis-server",
                                options=[],
                                placeholder="Choose a file",
                            ),
                        ],
                        label="Server Directory",
                    ),
                ]
            )
        ),
        dbc.ModalFooter(
            [
                dbc.Button("Apply", id="btn-confirm-analysis", color="primary"),
                dbc.Button("Cancel", id="btn-cancel-analysis", color="secondary"),
            ]
        ),
    ],
    id="modal-analysis",
    is_open=False,
    size="lg",
)
