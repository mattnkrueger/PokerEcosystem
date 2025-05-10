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
            # Hero section with responsive styling
            html.Div([
                html.Div(
                    html.Button(
                        html.I(className="fas fa-expand"),
                        id='fullscreen-button',
                        className='fullscreen-button',
                        title='Toggle fullscreen mode'
                    ),
                    className='fullscreen-button-container'
                ),
                html.H1("Krueger Poker Tracker", className="display-4 mb-4"),
                html.P(
                    "who tryna run ts",
                    className="lead mb-4"
                ),
                html.Hr(className="my-4"),
            ], className="hero-section mb-5 position-relative"),
            
            # Card sections for different features
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Start a New Game"),
                        dbc.CardBody([
                            html.P("Create a new poker game session and start tracking your plays."),
                            dbc.Button("Start Game", color="primary", href="/game", className="mt-3")
                        ], className="card-content")
                    ], className="h-100 mb-4 mb-md-0")
                ], md=4),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("View Stats"),
                        dbc.CardBody([
                            html.P("Check out your poker statistics and performance over time."),
                            dbc.Button("View Stats", color="secondary", href="/stats", className="mt-3")
                        ], className="card-content")
                    ], className="h-100 mb-4 mb-md-0")
                ], md=4),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Live Stream"),
                        dbc.CardBody([
                            html.P("Watch the current computer vision feed from the poker table."),
                            dbc.Button("View Live Stream", color="info", href="/live", className="mt-3")
                        ], className="card-content")
                    ], className="h-100")
                ], md=4),
            ], className="card-section"),
        ], className="home-content")
