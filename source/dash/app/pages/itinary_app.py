import dash
import dash_leaflet as dl
from dash import html, callback, Output, Input
import dash_bootstrap_components as dbc

from .components.form import display_form
from .components.itinary import ItinaryDisplay
from .components.map import display_map, ShowMap

dash.register_page(__name__, path='/demo')


layout = dbc.Container([
    dbc.Row([
        display_form()]
    ),
    html.Br(),
    dbc.Row([
        display_map()]
    ),
    html.Br(),
    dbc.Row(id='output'),
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
