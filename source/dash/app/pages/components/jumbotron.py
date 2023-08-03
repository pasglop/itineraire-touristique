import dash_bootstrap_components as dbc
from dash import html

jumbotron = html.Div(
    dbc.Container(
        [
            html.H1("Application d\'itinéraire Parisiens", className="display-3"),
            html.Img(src='https://i.goopics.net/brs6qu.jpg',
                     style={'width': '600px', 'height': '450px', 'display': 'block', 'margin': 'auto'}),
            html.P(
                "Réinventer les façons de découvrir Paris",
                className="lead",
            ),
            html.P(
                dbc.Button("Demo", href="/demo", size="lg", color="warning"), className="lead"
            ),
            html.Hr(className="my-2"),
            html.H3('Jean Beuzeval', style={'color': '#2c3e50', 'textAlign': 'center', 'font-family': 'Arial Black'}),
            html.H3('Marouen Arfaoui', style={'color': '#2c3e50', 'textAlign': 'center', 'font-family': 'Arial Black'}),
            html.H3('David Delpuech', style={'color': '#2c3e50', 'textAlign': 'center', 'font-family': 'Arial Black'}),
            html.Hr(className="my-2"),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)