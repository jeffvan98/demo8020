import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, title="About")

layout = dbc.Container([
    dbc.Row([
        html.H1("About", className="display-3"),
        html.P("This is a demonstration of the Dash framework for building interactive web applications.")
    ])
])