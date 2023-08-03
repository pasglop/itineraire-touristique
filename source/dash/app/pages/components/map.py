import random
from typing import Tuple, List, Dict, Any

import dash
from dash import callback, Output, Input
import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash_extensions.javascript import assign, Namespace

from ..utils.api import itinaryApi


def display_map():
    return dl.Map(id='map', children=[dl.TileLayer()], center=[48.8566, 2.3522], zoom=12,
                  style={'width': '100%', 'height': '50vh'})


class ShowMap:
    def __init__(self):
        self.markers = []
        self.hotel = None
        self.colors = [
            {'name': 'blue', 'hex': '#2A81CB'},
            {'name': 'gold', 'hex': '#FFD326'},
            {'name': 'red', 'hex': '#CB2B3E'},
            {'name': 'green', 'hex': '#2AAD27'},
            {'name': 'orange', 'hex': '#CB8427'},
            {'name': 'yellow', 'hex': '#CAC428'},
            {'name': 'violet', 'hex': '#9C2BCB'},
            {'name': 'grey', 'hex': '#7B7B7B'},
            {'name': 'black', 'hex': '#3D3D3D'}
        ]

    def get(self):
        return self.markers

    def display_hotel(self, hotel_poi):
        iti = itinaryApi()
        status, self.hotel = iti.get_poi_detail(hotel_poi)

        if status == 402:
            return {'error': self.hotel['detail']}

        name = f"Votre Hôtel : {self.hotel['address']}"
        markers = [dict(
            name=name,
            lat=self.hotel['latitude'],
            lon=self.hotel['longitude']
        )]
        geojson = dlx.dicts_to_geojson([{**m, **dict(tooltip=m['name'])} for m in markers])

        ns = Namespace("mapMarkerItinary", "hotel")

        # return [ dl.Marker(position=[self.hotel['latitude'], self.hotel['longitude']],
        #                        children=[dl.Tooltip(name)]
        #                            ) ]
        self.markers.append(dl.GeoJSON(data=geojson, options=dict(pointToLayer=ns("pointToLayer")), zoomToBounds=True))

        return self.get()

    def _pick_color(self):
        random_index = random.randint(0, len(self.colors) - 1)
        return self.colors.pop(random_index)

    def _process_itinary(self, poi_list: list):

        ns = Namespace("mapMarkerItinary", "other")

        for day in poi_list:
            geo_markers = []
            day_color = self._pick_color()
            positions = [[self.hotel['latitude'], self.hotel['longitude']]]
            for poi in day['pois']:
                geo_markers.append(dict(
                    name=poi['name'],
                    type=day_color['name'],
                    lat=poi['latitude'],
                    lon=poi['longitude']
                ))
                positions.append([poi['latitude'], poi['longitude']])

            positions.append([self.hotel['latitude'], self.hotel['longitude']])
            geojson = dlx.dicts_to_geojson([{**m, **dict(tooltip=m['name'])} for m in geo_markers])
            self.markers.append(dl.GeoJSON(data=geojson, options=dict(pointToLayer=ns("pointToLayer")), zoomToBounds=True))
            patterns = [dict(offset='12', repeat='25', dash=dict(pixelSize=10, pathOptions=dict(color=day_color['hex'], weight=3)))]
            self.markers.append(dl.PolylineDecorator(positions=positions, patterns=patterns))


    def display_itinary(self, hotel_poi, poi_list: list):
        self.display_hotel(hotel_poi)
        self._process_itinary(poi_list)
        return self.get()

        # for day in poi_list:
        #
        #     day_color = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(len(poi_list))])]
        #
        #     positions = [[self.hotel['latitude'], self.hotel['longitude']]]
        #     for poi in day['pois']:
        #         marker = dl.Marker(position=[poi['latitude'], poi['longitude']],
        #                        children=[dl.Tooltip(poi['name'])],
        #                            )
        #         positions.append([poi['latitude'], poi['longitude']])
        #         self.markers.append(marker)
        #
        #
        # return self.get()
