import dash_leaflet as dl
from dash import Output, Input

from source.dash.app.app import app
from source.dash.app.utils.map import generate_additional_markers


@app.callback(
    Output('map', 'children'),
    [Input('menu-deroulant', 'value')]
)
def afficher_hotel(val):
    children = [dl.TileLayer()]
    children.extend(generate_additional_markers())
    if val is not None:
        hotel = hotels_df.loc[val]
        children.append(dl.Marker(position=[hotel['latitude'], hotel['longitude']],
                                  children=[dl.Tooltip(hotel['name'] + '\n' + hotel['address'] + '\n' + hotel['website'])]))
    return children


@app.callback(
    Output('erreur-jours-visite', 'children'),
    [Input('jours-visite', 'value')]
)
def afficher_erreur_jours_visite(val):
    if val is not None and val > 10:
        return 'Veuillez sélectionner une valeur inférieure ou égale à 10'
    return ''
