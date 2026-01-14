from dash import callback, Input, Output, State, ctx
from src.initial_values import (
    INITIAL_PROJECT_JSON,
    INITIAL_UI_STATE,
    INITIAL_VALIDATION
)

# --- Helper functions (to be implemented later) ---
def handle_new_project():
    # returns updated project JSON
    pass

def handle_open_project(contents):
    pass

def handle_save_project(project):
    pass

def handle_save_as_project(project):
    pass

def handle_project_field_change(project, field, value):
    pass

def validate_project(project):
    # returns validation dict
    pass

def compute_ui_state(project, validation):
    # returns ui-state dict
    pass


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
    Input("project-name", "value"),
    Input("demographics-type", "value"),
    Input("demographics-value", "value"),
    Input("analysis-type", "value"),
    Input("analysis-value", "value"),
    Input("select-territories", "value"),
    Input("select-source-files", "value"),

    State("store-project-json", "data"),
)
def project_controller(
    new_clicks, open_clicks, save_clicks, save_as_clicks,
    project_name, demo_type, demo_value, analysis_type, analysis_value,
    territories, source_files,
    project
):
    # --- Detect what triggered the callback ---
    trigger = ctx.triggered_id

    # --- Dispatch to the correct handler ---
    if trigger == "btn-new-project":
        project = handle_new_project()

    elif trigger == "btn-open-project":
        project = handle_open_project(None)  # file contents later

    elif trigger == "btn-save-project":
        handle_save_project(project)

    elif trigger == "btn-save-as-project":
        handle_save_as_project(project)

    else:
        # A field changed — update project JSON
        project = handle_project_field_change(
            project,
            trigger,
            {
                "project-name": project_name,
                "demographics-type": demo_type,
                "demographics-value": demo_value,
                "analysis-type": analysis_type,
                "analysis-value": analysis_value,
                "select-territories": territories,
                "select-source-files": source_files,
            }.get(trigger)
        )

    # --- Validation ---
    validation = validate_project(project)

    # --- Compute UI state ---
    ui_state = compute_ui_state(project, validation)

    return project, ui_state, validation
