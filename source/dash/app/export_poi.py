from dash import dcc, html, Input, Output, callback
import pandas as pd
import requests
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

# ------- Adresse et port de l'API --------------------------------------------------

api_address = 'localhost'
api_port = 8000

# -------- Liste des catégories -----------------------------------------------------

cat_list = ['Restaurant', 'Hotel']

# -------- Format page web ----------------------------------------------------------

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

# -------- Layout -------------------------------------------------------------------

app.layout = html.Div(
    [
        html.H1('Exportation des données', 
        style={
            'textAlign': 'center', 
            'color': 'mediumturquoise'
            }
        ),
        dcc.Dropdown(
        id='cat_dropdown',
        options=[{'label':cat, 'value':cat} for cat in cat_list],
        value = cat_list[0],
        style={
            'width': '200px',
            "margin-block-start": "50px",
            "margin-block-end": "50px", 
            'background' : 'yellow'
            }
        ),
        html.Button("Download CSV", id="btn_csv"),
        dcc.Download(id="download-dataframe-csv")
    ]
)

# -------- Callbacks ----------------------------------------------------------------

@callback(
    Output("download-dataframe-csv", "data"),
    Input("btn_csv", "n_clicks"),
    Input("cat_dropdown", "value"),
    prevent_initial_call=True,
)
def func(n_clicks, cat):
    response = requests.get(
        url='http://{address}:{port}/poi_by_class/{classname}'.format(address=api_address, port=api_port, classname=cat)
    )
    dict_response = response.json()
    dict_list = dict_response['poi']
    df = pd.DataFrame.from_records(dict_list)
    return dcc.send_data_frame(df.to_csv, f"{cat}.csv")

# -------- Initialisation -----------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
