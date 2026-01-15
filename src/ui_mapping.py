from dash import callback, Input, Output, State
from src.project_ops import list_server_source_files

# open/close modals
@callback(
    Output("modal-add-source", "is_open"),
    Input("btn-add-source", "n_clicks"),
    Input("btn-cancel-add-source", "n_clicks"),
    State("modal-add-source", "is_open")
)
def toggle_add_source_modal(add_click, cancel_click, is_open):
    if add_click or cancel_click:
        return not is_open
    return is_open

@callback(
    Output("modal-demographics", "is_open"),
    Input("btn-open-demographics", "n_clicks"),
    Input("btn-cancel-demographics", "n_clicks"),
    State("modal-demographics", "is_open"),
)
def toggle_demographics_modal(open_click, cancel_click, is_open):
    if open_click or cancel_click:
        return not is_open
    return is_open

@callback(
    Output("modal-analysis", "is_open"),
    Input("btn-open-analysis", "n_clicks"),
    Input("btn-cancel-analysis", "n_clicks"),
    State("modal-analysis", "is_open"),
)
def toggle_analysis_modal(open_click, cancel_click, is_open):
    if open_click or cancel_click:
        return not is_open
    return is_open

# dropdowns
@callback(
    Output("dropdown-server-source", "options"),
    Input("btn-refresh-sources", "n_clicks")
)
def update_server_source_options(_):
    files = list_server_source_files()
    return [{"label": f, "value": f} for f in files]

@callback(
    Output("dropdown-server-source", "options"),
    Input("btn-refresh-sources", "n_clicks")
)
def update_server_source_options(_):
    files = list_server_source_files()
    return [{"label": f, "value": f} for f in files]

# enable/disable buttons
@callback(
    Output("btn-new-project", "disabled"),
    Input("store-ui-state", "data")
)
def map_add_source(ui_state):
    return ui_state["new_disabled"]

@callback(
    Output("btn-open-project", "disabled"),
    Input("store-ui-state", "data")
)
def map_add_source(ui_state):
    return ui_state["open_disabled"]

@callback(
    Output("btn-save-project", "disabled"),
    Input("store-ui-state", "data")
)
def map_add_source(ui_state):
    return ui_state["save_disabled"]

@callback(
    Output("btn-save-as-project", "disabled"),
    Input("store-ui-state", "data")
)
def map_add_source(ui_state):
    return ui_state["save_as_disabled"]

@callback(
    Output("btn-add-source", "disabled"),
    Input("store-ui-state", "data")
)
def map_add_source(ui_state):
    return ui_state["add_source_disabled"]

@callback(
    Output("btn-refresh-sources", "disabled"),
    Input("store-ui-state", "data")
)
def map_add_source(ui_state):
    return ui_state["refresh_sources_disabled"]

@callback(
    Output("btn-clear-sources", "disabled"),
    Input("store-ui-state", "data")
)
def map_add_source(ui_state):
    return ui_state["clear_sources_disabled"]

@callback(
    Output("btn-open-demographics", "disabled"),
    Input("store-ui-state", "data")
)
def map_add_source(ui_state):
    return ui_state["open_demographics_disabled"]

@callback(
    Output("btn-open-analysis", "disabled"),
    Input("store-ui-state", "data")
)
def map_add_source(ui_state):
    return ui_state["open_analysis_disabled"]

@callback(
    Output("btn-continue", "disabled"),
    Input("store-ui-state", "data")
)
def map_add_source(ui_state):
    return ui_state["continue_disabled"]

@callback(
    Output("btn-cancel", "disabled"),
    Input("store-ui-state", "data")
)
def map_add_source(ui_state):
    return ui_state["cancel_disabled"]