import random

import dash
from dash import callback, Output, Input
import dash_leaflet as dl
from dash_extensions.javascript import assign

from ..utils.api import itinaryApi


def display_map():
    return dl.Map(id='map', children=[dl.TileLayer()], center=[48.8566, 2.3522], zoom=12,
           style={'width': '100%', 'height': '50vh'})


class ShowMap:
    def __init__(self):
        self.markers = []

    def get(self):
        return self.markers

    def display_hotel(self, hotel_poi):
        iti = itinaryApi()
        status, poi = iti.get_poi_detail(hotel_poi)

        if status == 402:
            return {'error': poi['detail']}

        name = f"Votre Hôtel : {poi['address']}"
        marker = dl.Marker(position=[poi['latitude'], poi['longitude']],
                           children=[dl.Tooltip(name)])
        self.markers.append(marker)

    def display_itinary(self, hotel_poi, poi_list: list):
        self.display_hotel(hotel_poi)
        for day in poi_list:
            day_color = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
            for poi in day['pois']:
                marker = dl.Marker(position=[poi['latitude'], poi['longitude']],
                               children=[dl.Tooltip(poi['name'])])
                self.markers.append(marker)

        return self.get()
