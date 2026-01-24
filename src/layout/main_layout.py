from dash import html, dcc

from .modals import add_source_modal, demographics_modal, analysis_modal, modal_save_as, open_project_modal
from .project_panels import selections_panel, sources_list_panel, territory_selector, data_files_selector
from .buttons_bar import buttons_bar

from dash import html, dcc
#from .setup_screen import setup_screen_layout
#from .main_screen import main_screen_layout

setup_screen_layout = html.Div(
    [
        buttons_bar,
        sources_list_panel,
        territory_selector,
        data_files_selector,
    ]
)

main_screen_layout = html.Div(
    [
        html.Div("This will contain the main UI"),
    ]
)


main_layout = html.Div(
    [
        # Stores (global)
        dcc.Store(id="store-project-json"),
        dcc.Store(id="store-ui-state"),
        dcc.Store(id="store-validation"),
        dcc.Store(id="store-source-load-results", data=[]),
        dcc.Store(id="store-selections"),

        # Which screen is active
        dcc.Store(id="store-screen", data="setup"),

        # Download
        dcc.Download(id="download-project"),

        # Placeholder where screens will be rendered
        #html.Div(id="screen-container"),
        html.Div(id="screen-container", children=setup_screen_layout),

        # Modals (global)
        modal_save_as,
        open_project_modal,
        add_source_modal,
        demographics_modal,
        analysis_modal,
    ]
)


old_main_layout = html.Div(
    [
        # Stores
        dcc.Store(id="store-project-json"),
        dcc.Store(id="store-ui-state"),
        dcc.Store(id="store-validation"),
        dcc.Store(id="store-source-load-results", data=[]),
        dcc.Store(id="store-selections"),
        dcc.Download(id="download-project"),

        dcc.Store(id="store-screen", data="setup"),# or "main"
        # This is where the active screen will be rendered
        html.Div(id="screen-container"),

        buttons_bar,
        sources_list_panel,
        territory_selector,
        data_files_selector,

        # Modals
        modal_save_as,
        open_project_modal,
        add_source_modal,
        demographics_modal,
        analysis_modal,
    ]
)
