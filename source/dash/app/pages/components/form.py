from dash import Output, Input, callback, html, dcc

from source.dash.app.pages.utils.api import itinaryApi


def display_form():
    iti = itinaryApi()
    hotels_df = iti.get_hotel_dataframe()

    return html.Div([
        html.Label('Nombre de jours de visite'),
        dcc.Input(id='visitdays', type='number', min=1, max=10),
        html.Label('Sélectionnez votre hôtel'),
        dcc.Dropdown(id='basehotel',
                     options=[{'label': name, 'value': id} for id, name in zip(hotels_df['id'], hotels_df['name'])]),
        html.Button("Submit", id="submit-button", n_clicks=0),
        html.Div(id='erreur-jours-visite'),
    ])


@callback(
    Output('erreur-jours-visite', 'children'),
    [Input('visitdays', 'value')]
)
def afficher_erreur_jours_visite(val):
    if val is not None and val > 10:
        return 'Veuillez sélectionner une valeur inférieure ou égale à 10'
    return ''
