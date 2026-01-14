# src/state/initial_values.py

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
    "project_name_disabled": True,
    "save_disabled": True,
    "save_as_disabled": True,

    "add_source_disabled": True,
    "refresh_sources_disabled": True,

    "demographics_type_disabled": True,
    "demographics_value_disabled": True,

    "analysis_type_disabled": True,
    "analysis_value_disabled": True,

    "territories_disabled": True,
    "source_files_disabled": True,
    "clear_selections_disabled": True,

    "continue_disabled": True
}

INITIAL_VALIDATION = {
    "demographics_valid": False,
    "analysis_valid": False,
    "data_sources_valid": False,
    "selections_valid": False,
    "errors": []
}
