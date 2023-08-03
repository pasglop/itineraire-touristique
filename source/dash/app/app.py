import dash
from dash import Dash
from dash import dcc
from dash import html

external_stylesheets = [
    'https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap',  # Police calligraphique
    'https://fonts.googleapis.com/css2?family=Poppins:wght@800&display=swap',
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    'https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap'
]

app = Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True, use_pages=True)

app.layout = html.Div([
    html.H1('Multi-page app with Dash Pages'),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

    dash.page_container
])


if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
