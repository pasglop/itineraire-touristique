from dash import Output, Input, callback, html, dcc
import dash_bootstrap_components as dbc
from source.dash.app.pages.utils.api import itinaryApi


def display_form():
    iti = itinaryApi()
    hotels_df = iti.get_hotel_dataframe()

    form = dbc.Form(
        dbc.Row(
            [
                dbc.Label("Nombre de jours de visite", html_for="visitdays"),
                dbc.Col(
                    dcc.Input(id='visitdays', type='number', min=1, max=8),
                    className="me-2",
                ),

                dbc.Label("Sélectionnez votre hôtel", html_for="basehotel"),
                dbc.Col(
                    dcc.Dropdown(id='basehotel',
                                    options=[{'label': name, 'value': id} for id, name in
                                            zip(hotels_df['id'], hotels_df['name'])]),
                    className="me-2",
                ),
                dbc.Col(
                    dbc.Button("Submit", color="primary", id="submit-button", n_clicks=0)
                , width="auto"),
            ],
            className="g-3",
        )
    )

    return form
