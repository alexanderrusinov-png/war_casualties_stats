# src/state/initial_values.py
import os

INITIAL_PROJECT_JSON = {
    "project_file": "",
    "data_sources": [],
    "demographics": {
        "type": None,
        "value": None
    },
    "analysis_definitions": {
        "type": None,
        "value": None
    },
}

INITIAL_SELECTIONS_JSON = {
    "selected_territories": [],
    "selected_data_files": []
}

INITIAL_UI_STATE = {
    "new_disabled": False,
    "open_disabled": False,

    "save_disabled": True,
    "save_as_disabled": True,

    "add_source_disabled": True,
    "refresh_sources_disabled": True,
    "clear_sources_disabled": True,

    "open_demographics_disabled": True,
    "open_analysis_disabled": True,

    "continue_disabled": True,

    "territories_disabled": True,
    "source_files_disabled": True,
    "clear_selections_disabled": True
}

INITIAL_VALIDATION = {
    "demographics_file_valid": False,
    "load_errors": ["no sources specified"],
    "analysis_file_valid": False,
    "territories_with_demographic_data": [],
    "should_check_selections": False
}

# Paths to default files
DEFAULT_DEMOGRAPHICS_PATH = os.path.join(
    "data", "demographics", "default_demographics.json"
)

DEFAULT_ANALYSIS_PATH = os.path.join(
    "data", "analysis", "default_analysis.json"
)

SERVER_SOURCES_DIR = os.path.join("data", "data_sources")

