import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import numpy as np
import plotly.express as px
from datetime import datetime
import time

dash.register_page(__name__, title="Laboratory Turnaround Time")

def serve_layout():

    laboratory_services = [
        "Clinical Chemistry",
        "Hematology",
        "Microbiology",
        "Immunology and Serology",
        "Hemostasis and Coagulation Studies",
        "Blood Banking and Transfusion Medicine",
        "Molecular Diagnostics",
        "Cytology and Histology",
        "Urinalysis",
        "Toxicology",
        "Endocrinology",
        "Flow Cytometry",
        "Genetic Testing",
        "Point-of-Care Testing",
        "Allergy Testing"
    ]

    np.random.seed(int(time.time()))
    random_numbers = np.random.randint(0, 24*60, len(laboratory_services))
    fig = px.bar(
        x= laboratory_services,
        y=random_numbers, 
        labels={
            "x": "Laboratory Services",
            "y": "Turnaround Time (minutes)"
        })

    return dbc.Container([
        dbc.Row([
            html.H1("Laboratory Turnaround Time", className="display-3"),
            html.P("Objective: Assess the efficiency of laboratory services and ensure timely delivery of diagnostic information.")
        ]),
        dbc.Row(
            dcc.Graph(id="bar-chart", figure=fig)
        ),
        dbc.Row(
            html.Div([
                html.Hr(),
                html.Div("Report generated at: " + datetime.now().strftime("%A, %B %d, %Y %I:%M %p %z"))
            ], style={"textAlign": "center"})

        )

    ])

layout = serve_layout