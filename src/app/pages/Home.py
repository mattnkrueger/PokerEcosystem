import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash import callback, Input, Output
import plotly.express as px
import pandas as pd
from components.Card import Card
from components.StatsPreview import StatsPreview

class HomePage:
    """
    Landing page 
    """
    def __init__(self):
        self.name = "Home"
        self.path = "/"
        self.stats_preview = StatsPreview()
    
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
                html.H2("krueger poker tracker", className="mb-2"),
                html.P(
                    "super sick features that nobody asked for",
                    className="lead mb-3"
                ),
                html.Hr(className="my-3"),
            ], className="hero-section mb-4 position-relative"),
            
            # Main content area with cards and stats
            dbc.Row([
                # Left side - Cards in 2x2 grid
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            Card(
                                icon=html.Img(src="/assets/images/create_game.png", style={"height": "48px"}),
                                title="Create Game",
                                description="Create a new poker game session and start tracking your plays.",
                                button_text="Start Game",
                                button_href="/game"
                            )
                        ], md=6),
                        dbc.Col([
                            Card(
                                icon=html.Img(src="/assets/images/view_stats.png", style={"height": "48px"}),
                                title="View Stats",
                                description="Check out your poker statistics and performance over time.",
                                button_text="View Stats",
                                button_href="/stats"
                            )
                        ], md=6),
                    ], className="mb-3"),
                    dbc.Row([
                        dbc.Col([
                            Card(
                                icon=html.Img(src="/assets/images/view_camera.png", style={"height": "48px"}),
                                title="View Camera",
                                description="Watch the current computer vision feed from the poker table.",
                                button_text="View Live Stream",
                                button_href="/live"
                            )
                        ], md=6),
                        dbc.Col([
                            Card(
                                icon=html.Img(src="/assets/images/register_player.png", style={"height": "48px"}),
                                title="Register Player",
                                description="Add a new player to your poker ecosystem.",
                                button_text="Register Player",
                                button_href="/register"
                            )
                        ], md=6),
                    ])
                ], md=8),
                
                # Right side - Stats Preview
                dbc.Col([
                    self.stats_preview.layout()
                ], md=4)
            ], className="main-content")
        ], className="home-content")
