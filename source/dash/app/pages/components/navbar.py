import dash
from dash import html
from dash import Dash, callback, Output, Input, State
import dash_bootstrap_components as dbc

APP_LOGO = "/assets/logo.png"

demo_bar = dbc.Row(
    [
        dbc.Button(
            "Demo", color="warning", size="lg", href='/demo',  className="ms-4", n_clicks=0
        )
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=APP_LOGO, height="60px")),
                        dbc.Col(dbc.NavbarBrand("Itinéraires Parisiens", className="ms-3 font-weight-bold")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="http://localhost:8080/",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                demo_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="light",
    light=True,
)


# add callback for toggling the collapse on small screens
@callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open