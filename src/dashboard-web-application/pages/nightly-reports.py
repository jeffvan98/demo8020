import dash
from dash import html
import dash_bootstrap_components as dbc
from datetime import datetime
import os

dash.register_page(__name__, title="Nightly Reports")

def serve_layout():

    header_row = dbc.Row([
        html.H1("Nightly Reports", className="display-3"),
        html.P("Nightly reports provide a comprehensive overview of data generated on a daily basis.")
    ])

    footer_row = dbc.Row([
        html.Div([
            html.Hr(),
            html.Div("Report generated at: " + datetime.now().strftime("%A, %B %d, %Y %I:%M %p %z"))
        ], style={"textAlign": "center"})
    ])

    report_row = dbc.Row([
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

    if os.path.exists("assets/reports") and os.path.isdir("assets/reports"):

        files = os.listdir("assets/reports")    
        if "latest.html" in files:
            files.remove("latest.html")
        sorted_files = sorted(files, reverse=True)

        for index, file_name in enumerate(sorted_files):
            if index == 0:
                continue
            report_row.children.append(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H4(file_name.replace(".html", "")),
                            html.P("Reprted generated on " + file_name.replace(".html", ""), className="card-text"),
                            html.A("View Report", href=dash.get_asset_url("reports/" + file_name), className="btn btn-primary", target="_blank")
                        ])
                    )
                )
            )

            if index == 2:
                break

    return dbc.Container([
        header_row,
        report_row,
        footer_row
    ])

layout = serve_layout