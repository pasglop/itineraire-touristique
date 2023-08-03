import dash
import dash_leaflet as dl
from dash import html, callback, Output, Input

from .components.form import display_form
from .components.itinary import ItinaryDisplay
from .components.map import display_map, ShowMap

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
    [
        Output("output", "children"),
        Output("map", "children")],
    [
        Input("submit-button", "n_clicks"),
        Input("basehotel", "value")],
    [dash.dependencies.State("visitdays", "value")]
)
def update_output(n_clicks, basehotel, visitdays):
    itimap = ShowMap()
    maplayer = [dl.TileLayer()]
    if n_clicks > 0:
        # Here you can send a POST request with the entered data.
        iti = ItinaryDisplay(visitdays, basehotel)
        list_itinary = iti.generate_itinary()
        display_itinary = itimap.display_itinary(basehotel, iti.get_poi_list())

        maplayer.extend(display_itinary)

        return list_itinary, maplayer

    elif basehotel is not None:
        # call API POI with val
        maplayer.extend(itimap.display_hotel(basehotel))
        return {}, maplayer

    return {}, maplayer
