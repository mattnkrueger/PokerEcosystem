import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, dash_table

import plotly.express as px
import pandas as pd

def Navbar():
    navbar = html.Div(
        children=[
            # LHS
            html.Div("Krueger Poker", className="navbar-lhs"),

            # RHS
            html.Div([
                html.A("Home", href="/", className="navbar-link"),
                html.A("Game", href="/game", className="navbar-link"),
                html.A("Stats", href="/stats", className="navbar-link"),
                html.A("Live", href="/live", className="navbar-link"),
            ], className="navbar-rhs"),
        ],
        className="navbar"
    )
    
    return navbar