import dash
import pandas as pd
import dash_leaflet as dl
from dash import html, dcc

dash.register_page(__name__, path='/demo')

hotels_df = pd.DataFrame()

layout = html.Div([
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
    dl.Map(id='map', children=[dl.TileLayer()], center=[48.8566, 2.3522], zoom=10,
           style={'width': '100%', 'height': '50vh'}),
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
