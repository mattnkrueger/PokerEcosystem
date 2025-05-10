import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, dash_table

import plotly.express as px
import pandas as pd

def Footer():
    return html.Footer(
        html.Div(
            "Krueger 2025",
            className="footer-text"
        ),
        className="footer"
    )