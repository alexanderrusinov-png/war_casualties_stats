from dash import callback, Input, Output, State, ctx
from src.project_ops import handle_new_project, handle_project_field_change, handle_add_source, handle_clear_sources

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

    print ("computing ui state - project_exists = ", project_exists)

    ui["new_disabled"] =  project_exists
    ui["open_disabled"] =  project_exists

    ui["add_source_disabled"] = not project_exists
    ui["refresh_sources_disabled"] = not project_exists
    ui["refresh_sources_disabled"] = not project_exists
    ui["refresh_sources_disabled"] = not project_exists
    ui["refresh_sources_disabled"] = not project_exists
    ui["refresh_sources_disabled"] = not project_exists

    ui["add_source_disabled"] = not project_exists
    ui["refresh_sources_disabled"] = not project_exists
    ui["clear_sources_disabled"] = not project_exists,

    ui["open_demographics_disabled"] = not project_exists
    ui["open_analysis_disabled"] = not project_exists

    ui["continue_disabled"] = not project_exists
    ui["cancel_disabled"] = not project_exists

    # ... other UI rules go here ...

    print ("ui state = ", ui)
    return ui

# --- Controller callback ---
@callback(
    Output("store-project-json", "data"),
    Output("store-ui-state", "data"),
    Output("store-validation", "data"),

    Input("btn-new-project", "n_clicks"),
    Input("btn-open-project", "n_clicks"),
    Input("btn-save-project", "n_clicks"),
    Input("btn-save-as-project", "n_clicks"),

    # project fields
    State("store-project-json", "data"),
)

def project_controller(
    new_clicks, open_clicks, save_clicks, save_as_clicks,
    project
):

    # --- Detect what triggered the callback ---
    trigger = ctx.triggered_id
    print("project controller is called: ", trigger)

    # --- Dispatch to the correct handler ---
    if trigger == "btn-new-project":
        project = handle_new_project()
        print ("new project created:", project)

    elif trigger == "btn-open-project":
        project = handle_open_project(None)  # file contents later

    elif trigger == "btn-save-project":
        handle_save_project(project)

    elif trigger == "btn-save-as-project":
        handle_save_as_project(project)

    if trigger == "btn-add-source":
        new_source_value = ""
        project = handle_add_source(project, new_source_value)

    elif trigger == "btn-clear-sources":
        project = handle_clear_sources(project)

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

    return project, ui_state, validation
