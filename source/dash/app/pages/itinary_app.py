import dash
import dash_leaflet as dl
from dash import html, callback, Output, Input

from .components.form import display_form
from .components.itinary import ItinaryDisplay
from .components.map import display_map

dash.register_page(__name__, path='/demo')


layout = html.Div([
    html.H1('Démo de l\'application'),
    display_form(),
    html.Br(),
    html.Br(),
    display_map(),
    html.Br(),
    html.Div(id='output'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div([
        html.A('Revenir à la page d\'accueil', href='/', style={
            'font-family': 'Roboto',  # On peut remplacer Roboto par la police de notre choix
            'background-color': 'orange',
            'color': 'white',
            'padding': '10px 20px',
            'border-radius': '5px',
            'text-decoration': 'none',
            'font-weight': 'bold',
            'display': 'block',
            'text-align': 'center',
            'margin': 'auto',
            'width': '200px',
            'boxShadow': '0px 10px 20px 0px rgba(0,0,0,0.3)'  # Effet ombragé
        })
    ])
], style={'alignItems': 'center'})


@callback(
    Output("output", "children"),
    Input("submit-button", "n_clicks"),
    [dash.dependencies.State("visitdays", "value"),
     dash.dependencies.State("basehotel", "value")]
)
def update_output(n_clicks, visitdays, basehotel):
    if n_clicks > 0:
        # Here you can send a POST request with the entered data.
        iti = ItinaryDisplay()
        return iti.generate_itinary(visitdays, basehotel)

    return {}
