import flask
import dash
from dash import html
import dash_bootstrap_components as dbc
from os import environ

name = environ.get("DASHBOARD_WEB_APPLICATION_NAME", "Dashboard")
prefix = environ.get("DASHBOARD_WEB_APPLICATION_PREFIX", "/")

server = flask.Flask(__name__)
app = dash.Dash(
    __name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP], 
    server=server, 
    url_base_pathname=prefix, 
    use_pages=True)

app.layout = html.Div([
    dbc.NavbarSimple([
        dbc.NavLink("Home", href=prefix),
        dbc.DropdownMenu([            
            dbc.DropdownMenuItem("Efficiency Metrics", href=prefix + "efficiency-metrics"),
            dbc.DropdownMenuItem("Nightly Reports", href=prefix + "nightly-reports"),
        ], nav=True, in_navbar=True, label="Explore"),
        dbc.NavLink("About", href=prefix + "about"),
    ], brand=name, brand_href=prefix, color="dark", dark=True, links_left=True, style={"margin-bottom": "1rem"}),
    html.Div(dash.page_container)
])

if __name__ == "__main__":
    app.run_server(debug=True)