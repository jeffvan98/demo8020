import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, title="Nightly Reports")

layout = dbc.Container([
    dbc.Row([
        html.H1("Nightly Reports", className="display-3"),
        html.P("Nightly reports provide a comprehensive overview of data generated on a daily basis.")
    ]),
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Current"),
                    html.P("The data is meticulously gathered and analyzed, presenting a snapshot of the day's activities.", className="card-text"),
                    html.A("View Report", href=dash.get_asset_url("reports/latest.html"), className="btn btn-primary", target="_blank")
                ])
            )
        )
    ])
])