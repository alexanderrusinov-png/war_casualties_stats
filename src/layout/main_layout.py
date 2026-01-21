from dash import html, dcc

from .modals import add_source_modal, demographics_modal, analysis_modal
from .project_panels import selections_panel, sources_list_panel, territory_selector
from .buttons_bar import buttons_bar

project_layout = html.Div(
    [
        # Stores
        dcc.Store(id="store-project-json"),
        dcc.Store(id="store-ui-state"),
        dcc.Store(id="store-validation"),
        dcc.Store(id="store-source-load-results", data=[]),

        buttons_bar,
        sources_list_panel,
        territory_selector,
        #selections_panel,

        # Modals
        add_source_modal,
        demographics_modal,
        analysis_modal,
    ]
)
