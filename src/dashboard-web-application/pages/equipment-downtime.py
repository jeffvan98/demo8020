import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import numpy as np
import plotly.express as px
from datetime import datetime
import time

dash.register_page(__name__, title="Equipment Downtime")

def serve_layout():

    equipment_categories = [
        "Diagnostic",
        "Monitoring",
        "Life Support",
        "Surgical",
        "Laboratory",
        "Patient Beds and Furniture",
        "Rehabilitation and Therapy",
        "Patient Transport",
        "Pharmacy",
        "Radiation Therapy",
        "Emergency and Trauma",
        "IT and Healthcare Information Systems"
    ]

    np.random.seed(int(time.time()))
    random_numbers = np.random.randint(0, 31, len(equipment_categories))
    fig = px.bar(
        x=equipment_categories,
        y=random_numbers, 
        labels={
            "x": "Equipment Categories",
            "y": "Downtime (%)"
        })

    return dbc.Container([
        dbc.Row([
            html.H1("Equipment Downtime", className="display-3"),
            html.P("Objective: Minimize equipment downtime and ensure the availability of critical medical devices."),
            html.P(datetime.now())           
        ]),
        dbc.Row(
            dcc.Graph(id="bar-chart", figure=fig)
        )
    ])

layout = serve_layout