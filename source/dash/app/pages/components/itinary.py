from dash import html

from source.dash.app.utils.api import itinaryApi


def itinaryComponent(responseJson):
    raw_layout = []
    for day in responseJson['days']:
        for step in day['steps']:
            raw_layout.append(
                html.H4(step['name'])
            )
            raw_layout.append(
                html.P(step['instruction'])
            )

    return html.Div(raw_layout)

class ItinaryDisplay:
    def __init__(self):
        self.responseJson = None
        self.raw_layout = []
        self.layout = None

    def build(self):
        for day in self.responseJson['days']:
            for step in day['steps']:
                self.raw_layout.append(
                    html.H4(step['name'])
                )
                self.raw_layout.append(
                    html.P(step['instruction'])
                )
        self.layout = html.Div(self.raw_layout)

    def get(self):
        return self.layout

    def generate_itinary(self, visitdays, basehotel):
        iti = itinaryApi()
        self.responseJson = iti.create_itinary_response(visitdays, basehotel)
        if self.responseJson is not None:
            self.build()
            return self.get()
        return None
