# src/state/initial_values.py
import os

INITIAL_PROJECT_JSON = {
    "project_name": "",
    "data_sources": [],
    "demographics": {
        "type": None,
        "value": None
    },
    "analysis_definitions": {
        "type": None,
        "value": None
    },
    "selections": {
        "territories": [],
        "source_files": []
    }
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
    "demographics_valid": False,
    "analysis_valid": False,
    "data_sources_valid": False,
    "selections_valid": False,
    "errors": []
}

# Paths to default files
DEFAULT_DEMOGRAPHICS_PATH = os.path.join(
    "data", "demographics", "default_demographics.json"
)

DEFAULT_ANALYSIS_PATH = os.path.join(
    "data", "analysis", "default_analysis.json"
)

SERVER_SOURCES_DIR = os.path.join("data", "data_sources")

