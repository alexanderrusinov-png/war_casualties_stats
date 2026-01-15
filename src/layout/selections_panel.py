from dash import html, dcc
import dash_bootstrap_components as dbc

selections_panel = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Selections"),

            html.Label("Territories"),
            dcc.Dropdown(id="select-territories", multi=True),

            html.Br(),

            dbc.Button("Clear Selections", id="btn-clear-selections"),
        ]
    ),
    className="mb-3"
)
