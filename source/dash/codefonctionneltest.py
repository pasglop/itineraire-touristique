import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import dash_leaflet as dl
import pandas as pd

# Lire le fichier Excel dans le même dossier

file_name = 'hotel.xlsx'
hotels_df = pd.read_excel(file_name)

# Lire le fichier Excel pour les itinéraires
file_name_iti = 'iti.xlsx'
iti_df = pd.read_excel(file_name_iti)

external_stylesheets = [
    'https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap',  # Police calligraphique
    'https://fonts.googleapis.com/css2?family=Poppins:wght@800&display=swap',
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    'https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap'
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

def generate_additional_markers():
    markers = []
    for index, row in iti_df.iterrows():
        marker = dl.Marker(position=[row['end_latitude'], row['end_longitude']],
                           children=[dl.Tooltip(row['name'])])
        markers.append(marker)
    return markers

# Index page

index_page = html.Div([
    html.Div([
        html.A('Démo de l\'application', href='/page-3', style={
            'font-family': 'Roboto',
            'background-color': 'orange',
            'color': 'white',
            'padding': '10px 20px',
            'border-radius': '5px',
            'text-decoration': 'none',
            'font-weight': 'bold',
            'float': 'right',
            'margin': '10px',
            'boxShadow': '0px 10px 20px 0px rgba(0,0,0,0.3)'
        })
    ], style={'width': '100%', 'textAlign': 'right'}),
    html.Div([
        html.Img(src='https://i.goopics.net/brs6qu.jpg', style={'width': '600px', 'height': '450px', 'display': 'block', 'margin': 'auto'}),
        html.H1('Application d\'itinéraire de vacances', style={
            'color': '#34495e',
            'font-family': 'Poppins, sans-serif',
            'font-weight': '800',
            'text-align': 'center',
            'text-transform': 'uppercase',
            'font-size': '36px',
            'line-height': '46px',
            'margin-bottom': '30px',
            'padding': '15px',
            'background-color': '#f0e68c',
            'border-radius': '15px',
            'box-shadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
        }),
        html.H2('Réinventer les façons de voyager', style={
        'color': '#e74c3c',  # Couleur rouge vif
        'textAlign': 'center',
        'font-family': 'Great Vibes, cursive',  # Police à chasse fixe pour un look moderne
        'font-weight': 'bold',
        'font-size': '50px',
        'line-height': '34px',
        'margin-bottom': '20px',
        'padding': '10px',
        'border-radius': '10px',
    }),
        html.Br(),
        html.H3('Jean Beuzeval', style={'color': '#2c3e50', 'textAlign': 'center', 'font-family': 'Arial Black'}),
        html.H3('Marouen Arfaoui', style={'color': '#2c3e50', 'textAlign': 'center', 'font-family': 'Arial Black'}),
        html.H3('David Delpuech', style={'color': '#2c3e50', 'textAlign': 'center', 'font-family': 'Arial Black'}),
        html.Br(),
    ], style={'width': '600px', 'margin': 'auto'})  # Pour centrer l'ensemble de l'image, du titre et des sous-titres
], style={'alignItems': 'center'})

# Page 3
layout_3 = html.Div([
    html.H1('Démo de l\'application', style={'textAlign': 'center', 'color': 'mediumturquoise'}),
    html.Div([
        html.Div([
            html.Label('Nombre de jours de visite', style={'textAlign': 'center'}),
            dcc.Input(id='jours-visite', type='number', min=0, max=10, style={'width': '600px'}),
        ], style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center', 'marginRight': '20px'}),
        html.Div([
            html.Label('Sélectionnez votre hôtel', style={'textAlign': 'center'}),
            dcc.Dropdown(id='menu-deroulant',
                         options=[{'label': hotel['name'], 'value': index} for index, hotel in hotels_df.iterrows()],
                         style={'width': '600px'}),
        ], style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center', 'marginLeft': '20px'}),
    ], style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'}),
    html.Div(id='erreur-jours-visite', style={'color': 'red', 'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    dl.Map(id='map', children=[dl.TileLayer()], center=[48.8566, 2.3522], zoom=10, style={'width': '100%', 'height': '50vh'}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div([
    html.A('Revenir à la page d\'accueil', href='/', style={
        'font-family': 'Roboto',  # On peut remplacer Roboto par la police de notre choix
        'background-color': 'orange',
        'color': 'white',
        'padding': '10px 20px',
        'border-radius': '5px',
        'text-decoration': 'none',
        'font-weight': 'bold',
        'display': 'block',
        'text-align': 'center',
        'margin': 'auto',
        'width': '200px',
        'boxShadow': '0px 10px 20px 0px rgba(0,0,0,0.3)'  # Effet ombragé
    })
])
], style={'alignItems': 'center'})

@app.callback(
    Output('erreur-jours-visite', 'children'),
    [Input('jours-visite', 'value')]
)
def afficher_erreur_jours_visite(val):
    if val is not None and val > 10:
        return 'Veuillez sélectionner une valeur inférieure ou égale à 10'
    return ''

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

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-3':
        return layout_3
    else:
        return index_page

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
