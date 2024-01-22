import dash
from dash import html
import dash_bootstrap_components as dbc
from os import environ

dash.register_page(__name__, title="Efficency Metrics")
prefix = environ.get("DASHBOARD_WEB_APPLICATION_PREFIX", "/")

layout = dbc.Container([
    dbc.Row([
        html.H1("Efficiency Metrics", className="display-3"),
        html.P(
            "These reports are designed to measure and assess various factors related to resource utilization and operational effectiveness. "
            "The specific metrics included in these reports vary based on priorities and goals. ")
    ]),
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Equipment Downtime"),
                    html.P("Objective: Minimize equipment downtime and ensure the availability of critical medical devices.", className="card-text"),
                    dbc.Button("View Report", color="primary", href=prefix + "equipment-downtime")
                ])
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Laboratory Turnaround Time"),
                    html.P("Objective: Assess the efficiency of laboratory services and ensure timely delivery of diagnostic information.", className="card-text"),
                    dbc.Button("View Report", color="primary", href=prefix + "laboratory-turnaround-time")
                ])            
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Physician Productivity"),
                    html.P("Objective: Assess the workload and productivity of physicians to optimize staffing levels.", className="card-text"),
                    dbc.Button("View Report", color="primary", href=prefix + "physician-productivity")
                ])
            )
        )
    ])
])