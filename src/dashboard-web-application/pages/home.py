import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/", title="Home")

layout = dbc.Container([
    dbc.Row([
        html.H1("Welcome!", className="display-3"),
        html.P("Welcome to the healthcare analytics demonstration. This application is designed to showcase the capabilities of the Dash framework for building interactive web applications.")
    ])
])