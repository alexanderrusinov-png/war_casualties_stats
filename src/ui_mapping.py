from dash import callback, Input, Output, State, html, ctx
from src.project_ops import list_server_source_files, get_territories_list
from src.project_ops import list_server_directories, get_loaded_files_with_row_counts, get_list_of_relevant_source_files
import os
import json
import base64
import dash
from src.layout import main_layout


# open/close modals
@callback(
    Output("modal-add-source", "is_open"),
    Output("dropdown-server-source", "options"),
    Output("dropdown-server-dir", "options"),
    Input("btn-add-source", "n_clicks"),
    Input("btn-confirm-add-source", "n_clicks"),
    Input("btn-cancel-add-source", "n_clicks"),
    State("modal-add-source", "is_open")
)
def toggle_add_source_modal(open_click, ok_click, cancel_click, is_open):
    files = list_server_source_files()
    dirs = list_server_directories()

    if ok_click or cancel_click or open_click:
        return not is_open, [{"label": f, "value": f} for f in files], [{"label": d, "value": d} for d in dirs]

    return is_open, [{"label": f, "value": f} for f in files], [{"label": d, "value": d} for d in dirs]

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

# enable/disable buttons
@callback(
    Output("btn-new-project", "disabled"),
    Input("store-ui-state", "data")
)
def map_new_disabled(ui_state):
    return ui_state["new_disabled"]

@callback(
    Output("btn-open-project", "disabled"),
    Input("store-ui-state", "data")
)
def map_open_disabled(ui_state):
    return ui_state["open_disabled"]

@callback(
    Output("btn-save-project", "disabled"),
    Input("store-ui-state", "data")
)
def map_save_disabled(ui_state):
    return ui_state["save_disabled"]

@callback(
    Output("btn-save-as-project", "disabled"),
    Input("store-ui-state", "data")
)
def map_save_as_disabled(ui_state):
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
def map_refresh_sources(ui_state):
    return ui_state["refresh_sources_disabled"]

@callback(
    Output("btn-clear-sources", "disabled"),
    Input("store-ui-state", "data")
)
def map_clear_sources(ui_state):
    return ui_state["clear_sources_disabled"]


@callback(
    Output("btn-open-demographics", "disabled"),
    Input("store-ui-state", "data")
)
def map_open_demographics(ui_state):
    return ui_state["open_demographics_disabled"]

@callback(
    Output("btn-open-analysis", "disabled"),
    Input("store-ui-state", "data")
)
def map_open_analysis(ui_state):
    return ui_state["open_analysis_disabled"]

@callback(
    Output("btn-continue", "disabled"),
    Input("store-ui-state", "data")
)
def map_continue(ui_state):
    return ui_state["continue_disabled"]

@callback(
    Output("btn-cancel", "disabled"),
    Input("store-ui-state", "data")
)
def map_cancel(ui_state):
    return ui_state["cancel_disabled"]

# panels

def get_results_by_src(results, src):
    src_results = []

    for result in results:
        src_desc = src["type"]+":"+src["value"]
        if (result["src_description"] == src_desc):
            src_results.append(result)
    return src_results

def src_description_with_details(src, filename):
    res = src["type"] + ":" + src["value"]
    if src["type"] == "server-dir":
        res = res + ":" + filename
    return res

@callback(
    Output("div-sources-list", "children"),
    Input("store-source-load-results", "data"),
    State("store-project-json", "data"),
)
def render_sources_list(load_results, project):

    #print ("render sources list - started")

    if project is None:
        #print("render sources list - no project")
        return html.Div("No project defined")

    if not project["data_sources"]:
        #print("render sources list - no data sources")

        return html.Div("No sources added yet", style={"color": "orange"})

    rows_counts =  get_loaded_files_with_row_counts()

    #print("render sources list - data sources:")
    items = []
    for src in project["data_sources"]:
        #print("data source:", src)
        src_results = get_results_by_src(load_results, src)
        loaded = 0
        failed = 0
        for res in src_results:
            if res["status"] == "success":
                loaded += 1
            else:
                if res["file"] != "":
                    failed += 1

        msg = f"{loaded} files loaded, {failed} loads failed"
        items.append(html.Div(f"✓ {src['type']}: {src['value']} - {msg}", style={"font-weight": "bold"}))
        for res in src_results:
            if res["status"]== "success":
                desc = src_description_with_details(src, res["file"])
                cnt_value = rows_counts.get(desc, 0)
                msg_cnt = f"{cnt_value} rows loaded"

                items.append(html.Div(f"\u00A0\u00A0\u00A0\u00A0✓ {res['file']} - {msg_cnt} ", style={"color": "green"}))
            else:
                items.append(html.Div(f"\u00A0\u00A0\u00A0\u00A0✗ {res['file']} - {res['error']}", style={"color": "orange"}))

        loaded_cnt = get_loaded_files_with_row_counts()
        #print("loaded files:", loaded_cnt)

    return items


@callback(
    Output("dd-territories", "options"),
    Output("dd-territories", "value"),
    Output("div-territory-selection-status", "children"),
    Input("store-validation", "data"),
    State("store-project-json", "data"),
    State("dd-territories", "value")

)
def update_territories(validation, project_json, prev_selected):

    if validation is None:
        return dash.no_update, dash.no_update, dash.no_update

    # 1. Extract possible values from main data
    if project_json is None:
        possible = []
        selected = []
    else:
        possible = get_territories_list()
        # 2. Selection in project may be not updated!
        # selected = project_json.get("territories", [])
        if validation["should_check_selections"]:
            selected = project_json.get("selected_territories", [])
        else:
            if not prev_selected:
                selected = []
            else:
                selected = prev_selected

    #print("possible territories:", possible)
    #print("selected territories:", selected)

    # 3. Split into valid + invalid
    valid = [t for t in selected if t in possible]
    invalid = [t for t in selected if t not in possible]

    # 4. Build dropdown options
    options = [{"label": t, "value": t} for t in possible]

    # 5. Build status line
    status = []

    for t in valid:
        status.append(
            html.Span(
                t,
                style={"color": "green", "marginRight": "10px"}
            )
        )

    for t in invalid:
        status.append(
            html.Span(
                f"{t} (invalid)",
                style={"color": "red", "marginRight": "10px"}
            )
        )

    return options, valid, status

@callback(
    Output("dd-data-files", "options"),
    Output("dd-data-files", "value"),
    Output("div-data-files-selection-status", "children"),
    Input("dd-territories", "value"),
    State("store-validation", "data"),
    State("store-project-json", "data"),
    State("store-source-load-results", "data"),
    State("dd-data-files", "value")
)
def update_data_files(territories, validation, project_json, load_results, prev_selected):

    # 1. Extract possible values from main data
    if project_json is None:
        possible = []
        selected = []
        return dash.no_update, dash.no_update, dash.no_update
    else:
        possible = get_list_of_relevant_source_files(load_results, territories)
        #print ("relevant source files:", possible)
        # Selection in project may be  not updated!
        if validation["should_check_selections"]:
            selected = project_json.get("selected_data_files", [])
        else:
            if not prev_selected:
                selected = []
            else:
                selected = prev_selected

    # 3. Split into valid + invalid
    valid = [t for t in selected if t in possible]
    invalid = [t for t in selected if t not in possible]

    # 4. Build dropdown options
    rows_counts = get_list_of_relevant_source_files(load_results, territories)

    options = []
    for res in load_results:
        if res["status"] == "success":
            source = res["src_description"]
            left, right = source.split(":", 1)
            desc = src_description_with_details({"type": left, "value": right}, res["file"])
            cnt_value = rows_counts.get(desc, 0)
            if cnt_value != 0:
                msg_cnt = f"{desc} - {cnt_value}  relevant rows"
                #print(msg_cnt)
                options.append(desc)

    #print("options:", options)

    # 5. Build status line
    status = []

    for t in valid:
        status.append(
            html.Span(
                t,
                style={"color": "green", "marginRight": "10px"}
            )
        )

    for t in invalid:
        status.append(
            html.Span(
                f"{t} (invalid)",
                style={"color": "red", "marginRight": "10px"}
            )
        )

    return options, valid, status


@callback(
    Output("modal-save-as", "is_open"),
    Input("btn-save-project", "n_clicks"),
    Input("btn-save-as-project", "n_clicks"),
    Input("btn-save-as-confirm", "n_clicks"),
    Input("btn-save-as-cancel", "n_clicks"),
    State("store-project-json", "data"),
    State("modal-save-as", "is_open"),
    prevent_initial_call=True
)
def toggle_save_as_modal(save_click, save_as_click, confirm_click, cancel_click, project_json, is_open):
    trigger = ctx.triggered_id

    if not ctx.triggered:
        return False

    trigger = ctx.triggered[0]["prop_id"].split(".")[0]

    # Save button clicked
    if trigger == "btn-save-project":
        if not project_json:
            return False

        filename = project_json["project_file"]
        if filename:
            # filename exists → do NOT open modal
            return False
        else:
            # no filename → open modal
            return True

    # Save As button clicked → always open modal
    elif trigger == "btn-save-as-project":
        return True

    # Cancel button clicked → close modal
    if trigger == "btn-save-as-cancel":
        return False

    # Cancel button clicked → close modal
    if trigger == "btn-save-as-confirm":
        return False

    return is_open


@callback(
    Output("modal-open-project", "is_open"),
    Input("btn-open-project", "n_clicks"),
    Input("btn-open-project-cancel", "n_clicks"),
    Input("upload-project", "contents"),
    State("modal-open-project", "is_open"),
    prevent_initial_call=True
)
def toggle_open_project_modal(open_click, cancel_click, upload_project, is_open):

    trigger = ctx.triggered[0]["prop_id"].split(".")[0]

    if trigger == "btn-open-project":
        if open_click is None:
            return is_open
        return True

    if trigger == "btn-open-project-cancel":
        if cancel_click is None:
            return is_open
        return False

    if trigger == "upload-project":
        if upload_project is None:
            return is_open
        return False

    return is_open

@callback(
    Output("store-screen", "data"),
    Input("btn-continue", "n_clicks"),
    prevent_initial_call=True
)
def go_to_main(n):
    print("go_to_main", n)
    return "main"

@callback(
    Output("screen-container", "children"),
    Input("store-screen", "data")
)
def render_screen(screen):
    if screen == "setup":
        return main_layout.setup_screen_layout
    elif screen == "main":
        return main_layout.main_screen_layout

    return dash.no_update
