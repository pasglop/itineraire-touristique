from dash import callback, Output, Input

from source.dash.app.utils.map import generate_additional_markers


@callback(
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
