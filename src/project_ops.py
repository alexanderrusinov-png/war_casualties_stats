# src/project_ops.py

import json
import os
from src.initial_values import INITIAL_PROJECT_JSON, SERVER_SOURCES_DIR, DEFAULT_DEMOGRAPHICS_PATH, DEFAULT_ANALYSIS_PATH

def list_server_source_files():
    files = []
    for f in os.listdir(SERVER_SOURCES_DIR):
        if f.endswith(".csv"):
            files.append(f)
    return files

def list_server_directories():
    dirs = []
    for name in os.listdir(SERVER_SOURCES_DIR):
        full = os.path.join(SERVER_SOURCES_DIR, name)
        if os.path.isdir(full):
            dirs.append(name)
    return dirs

def load_json_file(path):
    """Utility to load a JSON file safely."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def handle_new_project():
    """
    Create a new project with default demographics and analysis definitions.
    Returns a fresh project JSON dict.
    """

    # Start from a clean template
    project = INITIAL_PROJECT_JSON.copy()

    # --- Load default demographics ---
    demo_data = load_json_file(DEFAULT_DEMOGRAPHICS_PATH)
    if demo_data is not None:
        project["demographics"] = {
            "type": "server_file",
            "value": DEFAULT_DEMOGRAPHICS_PATH
        }
    else:
        # If file missing, leave empty but valid
        project["demographics"] = {
            "type": None,
            "value": None
        }


    # --- Load default analysis definitions ---
    analysis_data = load_json_file(DEFAULT_ANALYSIS_PATH)
    if analysis_data is not None:
        project["analysis_definitions"] = {
            "type": "server_file",
            "value": DEFAULT_ANALYSIS_PATH
        }
    else:
        project["analysis_definitions"] = {
            "type": None,
            "value": None
        }

    # --- Reset selections ---
    project["selections"] = {
        "territories": [],
        "source_files": []
    }

    # --- Reset project name ---
    project["project_name"] = ""

    # --- Reset data sources ---
    project["data_sources"] = []

    return project

def handle_add_source(project, new_source):
    """
    Add a new data source to the project.
    new_source is expected to be a dict like:
    {
        "type": "server_file",
        "path": "/path/to/file.csv"
    }
    """
    if not new_source:
        return project

    # Ensure list exists
    if "data_sources" not in project or project["data_sources"] is None:
        project["data_sources"] = []

    # Avoid duplicates
    if new_source not in project["data_sources"]:
        project["data_sources"].append(new_source)

    return project


def handle_clear_sources(project):
    """
    Remove all data sources from the project.
    """
    project["data_sources"] = []

    # Also clear selections that depend on sources
    project["selections"]["source_files"] = []
    project["selections"]["territories"] = []

    return project

def handle_project_field_change(project, field, value):

    return project


