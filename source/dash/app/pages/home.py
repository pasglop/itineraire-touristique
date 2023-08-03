import dash

from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.Div([
        html.A('Démo de l\'application', href='/demo', style={
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
        html.Img(src='https://i.goopics.net/brs6qu.jpg',
                 style={'width': '600px', 'height': '450px', 'display': 'block', 'margin': 'auto'}),
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
