import dash
from dash import html
import dash_bootstrap_components as dbc

from ..utils.api import itinaryApi


class ItinaryDisplay:
    def __init__(self, visitdays, basehotel):
        self.responseJson = None
        self.raw_layout = []
        self.layout = None
        self.visit_days = visitdays
        self.base_hotel = basehotel

    def _build(self):
        day_layout = []
        for day_index, day in enumerate(self.responseJson['days']):
            self.raw_layout = []
            for step in day['steps']:
                match step['step_type']:
                    case 'Visiter':
                        self._visit_card(step)
                    case 'Marcher':
                        self._walk_card(step)
                    case 'Prendre le métro':
                        self._subway_card(step)

            day_layout.append(dbc.AccordionItem(
                self.raw_layout,
                title=f"Jour {day_index + 1}"
            ))

        self.layout = html.Div(
            dbc.Accordion(
                day_layout
            ))

    def _walk_card(self, step):
        self.raw_layout.append(
            html.Img(src=dash.get_asset_url('walking.png'))
        )

        self.raw_layout.append(
            html.H5(step['name'])
        )
        self.raw_layout.append(
            html.P(step['instruction'])
        )

    def _visit_card(self, step):

        body = [html.Img(src=dash.get_asset_url('map.png'), className="card-img-left", alt="..."),
                html.H4(f"Visiter {step['name']}", className="card-title"),
                html.H6(step['step_detail']['address'], className="card-subtitle"),
                html.P(step['step_detail']['description'], className="card-text")]
        if step['step_detail']['website'] is not None:
            body.append(
                dbc.CardLink("Site web", href=step['step_detail']['website'])
            )
        card = dbc.Card(
            dbc.CardBody(
                body
            ),
            style={"width": "100%"},
        )
        self.raw_layout.append(
            card
        )

    def _subway_card(self, step):

        self.raw_layout.append(
            html.Img(src=dash.get_asset_url('icons/metro.png'))
        )

        self.raw_layout.append(
            html.H5(step['name'])
        )
        self.raw_layout.append(
            html.P(step['instruction'])
        )

    def _day_header(self, day):
        self.raw_layout.append(f"Jour {day}")

    def get(self):
        return self.layout

    def generate_itinary(self):
        if self._get_itinary():
            self._build()
            return self.get()
        return None

    def _get_itinary(self) -> bool:
        if self.responseJson is not None:
            return True
        iti = itinaryApi()
        self.responseJson = iti.create_itinary_response(self.visit_days, self.base_hotel)
        if self.responseJson is not None:
            return True
        return False

    def get_poi_list(self):
        if self._get_itinary():
            list_pois = []
            for day_index, day in enumerate(self.responseJson['days']):
                poi = {
                    'day': day_index + 1,
                    'pois': []
                }
                for step in day['steps']:
                    if step['step_type'] == 'Visiter':
                        step['step_detail']['type'] = 'visit'
                        poi['pois'].append(step['step_detail'])
                    elif step['step_type'] == 'Prendre le métro':
                        step['step_detail']['name'] = step['name']
                        step['step_detail']['type'] = 'metro'
                        poi['pois'].append(step['step_detail'])
                list_pois.append(poi)

            return list_pois
