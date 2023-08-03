import json
import sys

import dash
import requests
from dash import Dash, Output, Input
from dash import dcc
from dash import html

from utils.api import itinaryApi

sys.path.append('..')

external_stylesheets = [
    'https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap',  # Police calligraphique
    'https://fonts.googleapis.com/css2?family=Poppins:wght@800&display=swap',
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    'https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap'
]

app = Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True, use_pages=True)

app.layout = html.Div([
    html.H1('Multi-page app with Dash Pages'),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

    dash.page_container
])


@app.callback(
    Output("output", "children"),
    Input("submit-button", "n_clicks"),
    [dash.dependencies.State("visitdays", "value"),
     dash.dependencies.State("basehotel", "value")]
)
def update_output(n_clicks, visitdays, basehotel):
    if n_clicks > 0:
        # Here you can send a POST request with the entered data.
        iti = itinaryApi()
        response = iti._createItinary(visitdays, basehotel)

        if response.status_code == 200:
            data = response.json()  # Update the store with the response.
            return json.dumps(data, indent=2)
        else:
            return f"Error: {response.text}"  # Update the store with the error message.
    return {}



if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
