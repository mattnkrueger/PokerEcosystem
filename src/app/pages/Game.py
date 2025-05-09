import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash import callback, Input, Output, State, dash_table
import plotly.express as px
import pandas as pd

class GamePage:
    """
    Game page
    """
    def __init__(self):
        self.name = "Game"
        self.path = "/game"

    def layout(self):
        return html.Div([
            html.H1("Game")
        ])