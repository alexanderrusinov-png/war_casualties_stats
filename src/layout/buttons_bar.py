from dash import html
import dash_bootstrap_components as dbc

buttons_bar_old = dbc.ButtonGroup(
    [
        dbc.Button("New", id="btn-new-project", color="primary"),
        dbc.Button("Open", id="btn-open-project"),
        dbc.Button("Save", id="btn-save-project"),
        dbc.Button("Save As", id="btn-save-as-project"),

        dbc.Button("Demographics", id="btn-open-demographics"),
        dbc.Button("Analysis", id="btn-open-analysis"),

        dbc.Button("Cancel", id="btn-cancel"),
        dbc.Button("Continue", id="btn-continue", color="success"),
    ],
    size="sm",
)

buttons_bar = dbc.Row(
    [
        # Left: the buttons
        dbc.Col(
            dbc.ButtonGroup(
                [
                    dbc.Button("New", id="btn-new-project", color="primary"),
                    dbc.Button("Open", id="btn-open-project"),
                    dbc.Button("Save", id="btn-save-project"),
                    dbc.Button("Save As", id="btn-save-as-project"),

                    dbc.Button("Demographics", id="btn-open-demographics"),
                    dbc.Button("Analysis", id="btn-open-analysis"),

                    dbc.Button("Cancel", id="btn-cancel"),
                    dbc.Button("Continue", id="btn-continue", color="success"),
                ],
                size="sm",
            ),
            width="auto",
        ),

        # Right: dynamic file info
        dbc.Col(
            html.Div(
                id="div-demographics-analysis-info",
                style={
                    "paddingLeft": "20px",
                    "fontSize": "1.0rem",
                    "color": "#999",
                    "whiteSpace": "nowrap",
                },
            ),
            width="auto",
            align="center",
        ),
    ],
    align="center",
    className="mb-2",
)


sources_buttons_bar = dbc.ButtonGroup(
    [
        dbc.Button("Add Source", id="btn-add-source", color = "dark"),
        dbc.Button("Refresh Sources", id="btn-refresh-sources", color = "dark"),
        dbc.Button("Clear Sources", id="btn-clear-sources", color = "dark"),
    ],
    size="sm",
)


