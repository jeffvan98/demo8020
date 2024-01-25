import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import numpy as np
import plotly.express as px
from datetime import datetime
import time

dash.register_page(__name__, title="Physician Productivity")

def serve_layout():

    specialties = [
        "Cardiology",
        "Dermatology",
        "Endocrinology",
        "Gastroenterology",
        "Hematology",
        "Infectious Disease",
        "Nephrology",
        "Neurology",
        "Obstetrics and Gynecology",
        "Opthalmology",
        "Otolaryngology",
        "Pediatrics",
        "Pulmonology",
        "Psychiatry",
        "Radiology",
        "Rheumatology",
        "Urology",
        "Allergy and Immunology",
        "Emergency Medicine"
    ]

    np.random.seed(int(time.time()))
    random_numbers = np.random.randint(75, 101, len(specialties))
    fig = px.bar(
        x= specialties,
        y=random_numbers, 
        labels={
            "x": "Specialty",
            "y": "Productivity (%)"
        })

    return dbc.Container([
        dbc.Row([
            html.H1("Physician Productivity", className="display-3"),
            html.P("Objective: Assess the workload and productivity of physicians to optimize staffing levels.")
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