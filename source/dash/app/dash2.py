import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_leaflet as dl

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

index_page = html.Div([
    html.Img(src='https://i.goopics.net/brs6qu.jpg', style={'width': '400px', 'height': '400px', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
    html.H1('Application d\'itinéraire de vacances', style={'color': '#2c3e50', 'textAlign': 'center', 'font-family': 'Arial Black'}),
    html.Br(),
    html.H2('Réalisée en langage Python', style={'color': '#2c3e50', 'textAlign': 'center', 'font-family': 'Arial Black'}),
    html.Br(),
    html.H3('Jean Beuzeval', style={'color': '#2c3e50', 'textAlign': 'center', 'font-family': 'Arial Black'}),
    html.H3('Marouen Arfaoui', style={'color': '#2c3e50', 'textAlign': 'center', 'font-family': 'Arial Black'}),
    html.H3('David Delpuech', style={'color': '#2c3e50', 'textAlign': 'center', 'font-family': 'Arial Black'}),
    html.Br(),
    html.Button(dcc.Link('Démo de l\'application', href='/page-3'))
], style={'alignItems': 'center'})

# Page 3
layout_3 = html.Div([
    html.H1('Démo de l\'application', style={'textAlign': 'center', 'color': 'mediumturquoise'}),
    html.Div([
        html.Div([
            html.Label('Nombre de jours de visite', style={'textAlign': 'center'}),
            dcc.Input(id='jours-visite', type='number', min=0, max=10, style={'width': '200px'}),
        ], style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center', 'marginRight': '20px'}),
        html.Div([
            html.Label('Sélectionnez votre hôtel', style={'textAlign': 'center'}),
            dcc.Dropdown(id='menu-deroulant',
                         options=[{'label': 'Option ' + str(i), 'value': i} for i in range(1, 6)],
                         style={'width': '200px'}),
        ], style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center', 'marginLeft': '20px'}),
    ], style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'}),
    html.Div(id='erreur-jours-visite', style={'color': 'red', 'textAlign': 'center'}),
    html.Br(),  # Saut de ligne ajouté
    html.Br(),  # Saut de ligne ajouté
    # Ajout de la carte OpenStreetMap
    dl.Map([dl.TileLayer()], center=[48.8566, 2.3522], zoom=10, style={'width': '100%', 'height': '50vh'}),
    html.Br(),
    html.Br(),
    html.Div([
        html.Button(dcc.Link('Revenir à la page d\'accueil', href='/'), style={'display': 'block', 'margin': 'auto'})
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