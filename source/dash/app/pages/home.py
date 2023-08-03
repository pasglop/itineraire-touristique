import dash

from dash import html

from .components.jumbotron import jumbotron

dash.register_page(__name__, path='/')

layout = html.Div([
    jumbotron
], style={'alignItems': 'center'})
