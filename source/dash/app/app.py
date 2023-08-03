import dash
from dash import Dash
from dash import html
import dash_bootstrap_components as dbc

from pages.components.navbar import navbar

external_stylesheets = [
    dbc.themes.FLATLY
]


app = Dash(__name__, external_stylesheets=external_stylesheets, use_pages=True)

app.layout = html.Div([
    navbar,
    dbc.Container([
        dash.page_container
    ]
    , className="pt-4 pb-4", fluid=True),

])


if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
