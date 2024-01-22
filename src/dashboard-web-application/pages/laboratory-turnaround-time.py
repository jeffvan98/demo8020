import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import numpy as np
import plotly.express as px

dash.register_page(__name__, title="Laboratory Turnaround Time")

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

np.random.seed(42)
random_numbers = np.random.randint(0, 24*60, len(laboratory_services))
fig = px.bar(
    x= laboratory_services,
    y=random_numbers, 
    labels={
        "x": "Laboratory Services",
        "y": "Turnaround Time (minutes)"
    })

layout = dbc.Container([
    dbc.Row([
        html.H1("Laboratory Turnaround Time", className="display-3"),
        html.P("Objective: Assess the efficiency of laboratory services and ensure timely delivery of diagnostic information.")
    ]),
    dbc.Row(
        dcc.Graph(id="bar-chart", figure=fig)
    )
])