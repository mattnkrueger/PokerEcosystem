import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash import callback, Input, Output
import plotly.express as px
import pandas as pd

class HomePage:
    """
    Landing page 
    """
    def __init__(self):
        self.name = "Home"
        self.path = "/"
    
    def layout(self):
        return html.Div([
            html.H1("Home Page", className="mb-4"),
            dbc.Card([
                dbc.CardHeader("Start a New Game"),
                dbc.CardBody([
                    html.P("Create a new poker game session and start tracking your plays."),
                    dbc.Button("Start Game", color="primary", href="/game")
                ])
            ]),
            dbc.Card([
                dbc.CardHeader("View Stats"),
                dbc.CardBody([
                    html.P("Check out your poker statistics and performance over time."),
                    dbc.Button("View Stats", color="secondary", href="/stats")
                ])
            ]),
            dbc.Card([
                dbc.CardHeader("Live Stream"),
                dbc.CardBody([
                    html.P("Watch the current computer vision feed from the poker table."),
                    dbc.Button("View Live Stream", color="info", href="/live")
                ])
            ])
        ])
