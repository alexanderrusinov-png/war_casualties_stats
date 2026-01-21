from dash import callback, Input, Output, State, html
from src.project_ops import list_server_source_files
from src.project_ops import list_server_directories, get_loaded_files_with_row_counts
import os

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

    print ("render sources list - started")

    if project is None:
        print("render sources list - no project")
        return html.Div("No project defined")

    if not project["data_sources"]:
        print("render sources list - no data sources")

        return html.Div("No sources added yet", style={"color": "orange"})

    rows_counts = get_loaded_files_with_row_counts()

    print("render sources list - data sources:")
    items = []
    for src in project["data_sources"]:
        print("data source:", src)
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
        print("loaded files:", loaded_cnt)

    return items
