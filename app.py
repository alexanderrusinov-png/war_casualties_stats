import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
# callbacks:
from src import project_controller
from src import ui_mapping
import os

def collect_ids(component):
    ids = []
    if hasattr(component, "id") and component.id:
        ids.append(component.id)
    if hasattr(component, "children"):
        children = component.children
        if isinstance(children, list):
            for c in children:
                ids.extend(collect_ids(c))
        else:
            ids.extend(collect_ids(children))
    return ids

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
#app.config.suppress_callback_exceptions = True

from src.layout import main_layout

#app.layout = main_layout.project_layout
app.layout = main_layout.main_layout

app.validation_layout = html.Div([
    main_layout.main_layout,
    main_layout.setup_screen_layout,
    main_layout.main_screen_layout,
])

print("VALIDATION LAYOUT IDs:")

print(collect_ids(app.validation_layout))


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