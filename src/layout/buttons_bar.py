from dash import html
import dash_bootstrap_components as dbc

buttons_bar = dbc.ButtonGroup(
    [
        dbc.Button("New", id="btn-new-project", color="primary"),
        dbc.Button("Open", id="btn-open-project"),
        dbc.Button("Save", id="btn-save-project"),
        dbc.Button("Save As", id="btn-save-as-project"),

        dbc.Button("Add Sources", id="btn-add-source"),
        dbc.Button("Clear Sources", id="btn-clear-sources"),
        dbc.Button("Refresh Sources", id="btn-refresh-sources"),

        dbc.Button("Demographics", id="btn-open-demographics"),
        dbc.Button("Analysis", id="btn-open-analysis"),

        dbc.Button("Cancel", id="btn-cancel"),
        dbc.Button("Continue", id="btn-continue", color="success"),
    ],
    size="sm",
)

