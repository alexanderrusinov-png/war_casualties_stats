from dash import html, dcc

from .modals import add_source_modal, demographics_modal, analysis_modal
from .selections_panel import selections_panel
from .buttons_bar import buttons_bar

project_layout = html.Div(
    [
        # Stores
        dcc.Store(id="store-project-json"),
        dcc.Store(id="store-ui-state"),
        dcc.Store(id="store-validation"),

        buttons_bar,
        selections_panel,

        # Modals
        add_source_modal,
        demographics_modal,
        analysis_modal,
    ]
)
