import dash
from dash import Dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

external_stylesheets = [
    dbc.themes.SIMPLEX
]

app = Dash(__name__, external_stylesheets=external_stylesheets, use_pages=True)

app.layout = html.Div([
    dash.page_container
])


if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
