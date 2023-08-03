from dash import html

from source.dash.app.pages.utils.api import itinaryApi



class ItinaryDisplay:
    def __init__(self):
        self.responseJson = None
        self.raw_layout = []
        self.layout = None

    def _build(self):
        for day_index, day in enumerate(self.responseJson['days']):
            self._day_header(day_index + 1)
            for step in day['steps']:
                match step['step_type']:
                    case 'Visiter':
                        self._visit_card(step)
                    case 'Marcher':
                        self._walk_card(step)
                    case 'Prendre le métro':
                        self._subway_card(step)

        self.layout = html.Div(self.raw_layout)

    def _walk_card(self, step):
        self.raw_layout.append(
            html.H4(step['name'])
        )
        self.raw_layout.append(
            html.P(step['instruction'])
        )

    def _visit_card(self, step):
        self.raw_layout.append(
            html.H4(step['name'])
        )
        self.raw_layout.append(
            html.P(step['instruction'])
        )

    def _subway_card(self, step):
        self.raw_layout.append(
            html.H4(step['name'])
        )
        self.raw_layout.append(
            html.P(step['instruction'])
        )

    def _day_header(self, day):
        self.raw_layout.append(f"Jour {day}")

    def get(self):
        return self.layout

    def generate_itinary(self, visitdays, basehotel):
        iti = itinaryApi()
        self.responseJson = iti.create_itinary_response(visitdays, basehotel)
        if self.responseJson is not None:
            self._build()
            self.process_poi()
            return self.get()
        return None

    def process_poi(self):
        pass
