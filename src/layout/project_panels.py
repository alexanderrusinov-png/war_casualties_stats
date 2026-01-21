from dash import html, dcc
import dash_bootstrap_components as dbc
from src.layout.buttons_bar import sources_buttons_bar

sources_list_panel = dbc.Card(
    [
        #dbc.CardHeader("Sources", style={"fontSize": "1.1rem", "fontWeight": "500","padding": "6px 12px"}),
        dbc.CardBody(
            [
                sources_buttons_bar,
                # This is the container your callback updates
                html.Div(
                    id="div-sources-list",
                    style={
                        "maxHeight": "300px",
                        "overflowY": "auto",
                        "paddingLeft": "5px"
                    }
                ),
            ],
            style={"paddingTop": "8px", "paddingBottom": "8px"}
        ),
    ],
    className="mb-3"
)

territory_selector = html.Div(
    [
        html.Label("Select Territories", style={"fontWeight": "600"}),

        dcc.Dropdown(
            id="dd-territories",
            options=[],          # filled dynamically
            multi=True,
            placeholder="Choose territories...",
        ),

        html.Div(
            id="div-territory-selection-status",
            style={"marginTop": "8px", "fontSize": "0.9rem"},
        ),
    ]
)



selections_panel = dbc.Card(
    dbc.CardBody(
        [
            html.Label("Select Territories"),
            dcc.Dropdown(id="select-territories", multi=True),

            html.Br(),

            dbc.Button("Clear Selections", id="btn-clear-selections"),
        ]
    ),
    id = "selections-list",
    className="mb-3"
)