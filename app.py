import dash
from dash import Dash
import dash_bootstrap_components as dbc
from src.layout import main_layout

# callbacks:
from src import project_controller
from src import ui_mapping
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEFAULT_DEMOGRAPHICS_PATH = os.path.join(
    BASE_DIR, "data", "demographics", "default_demographics.json"
)

DEFAULT_ANALYSIS_PATH = os.path.join(
    BASE_DIR, "data", "analysis", "default_analysis.json"
)

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
app.layout = main_layout.project_layout

app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            body {
                font-size: 0.9rem;  /* smaller than Bootstrap default */
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>

"""

# register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)