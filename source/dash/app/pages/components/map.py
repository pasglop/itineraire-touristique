import dash
from dash import callback, Output, Input
import dash_leaflet as dl

from ..utils.api import itinaryApi


def display_map():
    return dl.Map(id='map', children=[dl.TileLayer()], center=[48.8566, 2.3522], zoom=12,
           style={'width': '100%', 'height': '50vh'})

def generate_additional_markers(name: str, lat: float, long: float):
    markers = []
    marker = dl.Marker(position=[lat, long],
                       children=[dl.Tooltip(name)])
    markers.append(marker)

    return markers


@callback(
    Output('map', 'children'),
    [Input('basehotel', 'value')]
)
def afficher_hotel(val):
    children = [dl.TileLayer()]
    if val is not None:
        # call API POI with val
        iti = itinaryApi()
        status, poi = iti.get_poi_detail(val)

        if status == 402:
            return poi['detail']

        children.extend(generate_additional_markers(poi['name'], poi['latitude'], poi['longitude']))

    return children
