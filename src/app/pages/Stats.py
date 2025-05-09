import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash import callback, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

class StatsPage:
    """
    Stats page
    """
    def __init__(self):
        self.name = "Stats"
        self.path = "/stats"
    
    def layout(self):
        return html.Div([
            html.H1("Stats")
        ])