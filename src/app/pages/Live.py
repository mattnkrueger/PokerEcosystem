import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash import callback, Input, Output
import plotly.express as px
import pandas as pd

class LivePage:
    """
    Live page
    """
    def __init__(self):
        self.name = "Live"
        self.path = "/live"
    
    def layout(self):
        return html.Div([
            html.H1("Live")
        ])