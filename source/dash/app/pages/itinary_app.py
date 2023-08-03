import dash
import pandas as pd
import dash_leaflet as dl
from dash import html, dcc, Output, Input

from source.dash.app import app
from source.dash.app.utils.api import itinaryApi

dash.register_page(__name__, path='/demo')

iti = itinaryApi()
hotels_df = iti.getHotelDataframe()

layout = html.Div([
    html.H1('Démo de l\'application'),
    html.Div([
        html.Label('Nombre de jours de visite'),
        dcc.Input(id='visitdays', type='number', min=1, max=10),
        html.Label('Sélectionnez votre hôtel'),
        dcc.Dropdown(id='basehotel',
                     options=[{'label': name, 'value': id} for id, name in zip(hotels_df['id'], hotels_df['name'])]),
        html.Button("Submit", id="submit-button", n_clicks=0)
    ]),

    html.Div(id='erreur-jours-visite'),
    html.Br(),
    html.Br(),
    dl.Map(id='map', children=[dl.TileLayer()], center=[48.8566, 2.3522], zoom=10,
           style={'width': '100%', 'height': '50vh'}),
    html.Br(),
    html.Div(id='output'),
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
