import dash
from dash import callback, Input, Output, State, ctx
from src.project_ops import handle_new_project, handle_project_field_change, handle_add_source, handle_clear_sources, handle_refresh_sources

from src.initial_values import (
    INITIAL_PROJECT_JSON,
    INITIAL_UI_STATE,
    INITIAL_VALIDATION
)

# --- Helper functions (to be implemented later) ---
#def handle_new_project():
    # returns updated project JSON
 #   pass

def handle_open_project(contents):
    return {}

def handle_save_project(project):
    pass

def handle_save_as_project(project):
    pass

#def handle_project_field_change(project, field, value):
#    return project

def validate_project(project):
    # returns validation dict
    return {}


def compute_ui_state(project, validation):
    ui = INITIAL_UI_STATE.copy()

    # --- Add Source and Refresh Sources ---
    # Enabled whenever a project exists (new or loaded)
    project_exists = project is not None

    has_sources = False
    if project_exists:
        if  (project["data_sources"]) and (project["data_sources"] != []):
            has_sources = True

    #print ("computing ui state - project_exists = ", project_exists)

    ui["new_disabled"] =  project_exists
    ui["open_disabled"] =  project_exists

    ui["save_disabled"] =  not project_exists
    ui["save_as_disabled"] = not project_exists
    ui["cancel_disabled"] = not project_exists

    ui["add_source_disabled"] =  not project_exists

    ui["refresh_sources_disabled"] = not has_sources
    ui["clear_sources_disabled"] = not has_sources

    ui["open_demographics_disabled"] =  not project_exists
    ui["open_analysis_disabled"] =  not project_exists

    ui["continue_disabled"] = not project_exists

    # ... other UI rules go here ...
    print ("ui state = ", ui)
    return ui

@callback(
    Output("div-demographics-analysis-info", "children"),
    Input("store-project-json", "data")
)
def update_file_info(project_json):
    if not project_json:
        return ""

    demo = project_json.get("demographics")
    print ("demographics file", demo)

    analysis = project_json.get("analysis_definitions")
    print("analysis file", analysis)

    parts = []

    if demo:
        parts.append(
            f"Demographics: {demo['type']}, {demo['value']}"
        )

    if analysis:
        parts.append(
            f"Analysis: {analysis['type']}, {analysis['value']}"
        )

    return " | ".join(parts)


# --- Controller callback ---
@callback(
    Output("store-project-json", "data"),
    Output("store-ui-state", "data"),
    Output("store-validation", "data"),
    Output("store-source-load-results", "data"),

    Input("btn-new-project", "n_clicks"),
    Input("btn-open-project", "n_clicks"),
    Input("btn-save-project", "n_clicks"),
    Input("btn-save-as-project", "n_clicks"),
    Input("btn-confirm-add-source", "n_clicks"),
    Input("btn-refresh-sources", "n_clicks"),
    Input("btn-clear-sources", "n_clicks"),

    State("tabs-add-source", "active_tab"),
    State("upload-local-source", "contents"),
    State("upload-local-source", "filename"),
    State("input-url-source", "value"),
    State("dropdown-server-source", "value"),
    State("dropdown-server-dir", "value"),

    # project fields
    State("store-project-json", "data"),
    State("store-source-load-results", "data"),
)

def project_controller(
    new_clicks, open_clicks, save_clicks, save_as_clicks,
    add_source_clicks, refresh_sources_click, clear_sources_click, source_tab, local_content, local_filename, input_url, server_file, server_dir,
    project, all_results
):

    # --- Detect what triggered the callback ---
    trigger = ctx.triggered_id
    #print("project controller is called: ", trigger)

    results_changed = False

    # --- Dispatch to the correct handler ---
    if trigger == "btn-new-project":
        project = handle_new_project()
        print ("new project created:", project)
        results_changed = True
        all_results = []

    elif trigger == "btn-open-project":
        project = handle_open_project(None)  # file contents later

    elif trigger == "btn-save-project":
        handle_save_project(project)

    elif trigger == "btn-save-as-project":
        handle_save_as_project(project)

    if trigger == "btn-confirm-add-source":
        source = {
            "type": "undefined"
        }

        #print ("adding source: " + source_tab)
        if source_tab == "tab-local":
            source = {
                "type": "local-file",
                "value": local_filename,
                "content": local_content
            }

        elif source_tab == "tab-url":
            source = {
                "type": "url",
                "value": input_url
            }

        elif source_tab == "tab-server-file":
            source = {
                "type": "server-file",
                "value": server_file
            }

        elif source_tab == "tab-server-dir":
            source = {
                "type": "server-dir",
                "value": server_dir
            }

        project, load_results = handle_add_source(project, source)
        #print("results before:", all_results)
        #print("new results", load_results)
        all_results.extend (load_results)
        #print("results after:", all_results)
        results_changed = True

    elif trigger == "btn-clear-sources":
        project = handle_clear_sources(project)
        all_results = []
        results_changed = True

    elif trigger == "btn-refresh-sources":
        project, all_results = handle_refresh_sources(project)
        results_changed = True

    else:
        # A field changed — update project JSON
        project = handle_project_field_change(
            project,
            trigger,
            ""
        )

    # --- Validation ---
    validation = validate_project(project)

    # --- Compute UI state ---
    ui_state = compute_ui_state(project, validation)

    if results_changed:
        return project, ui_state, validation, all_results
    else:
        return project, ui_state, validation, dash.no_update