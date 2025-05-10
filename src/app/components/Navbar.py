import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, dash_table, callback_context

import plotly.express as px
import pandas as pd

def Navbar():
    # Get current pathname to determine active link
    @callback(
        Output("home-nav", "className"),
        Output("game-nav", "className"),
        Output("stats-nav", "className"),
        Output("live-nav", "className"),
        Input("url", "pathname")
    )
    def update_active_links(pathname):
        if pathname is None:
            pathname = "/"
            
        # Normalize pathname
        if not pathname.endswith('/'):
            pathname = pathname + '/'
        if pathname != '/' and len(pathname) > 1 and pathname.endswith('/'):
            pathname = pathname[:-1]
            
        # Base classname
        base_class = "navbar-link-container"
        
        # Set active class based on pathname
        home_class = f"{base_class} home active" if pathname == "/" else f"{base_class} home"
        game_class = f"{base_class} game active" if pathname == "/game" else f"{base_class} game"
        stats_class = f"{base_class} stats active" if pathname == "/stats" else f"{base_class} stats"
        live_class = f"{base_class} live active" if pathname == "/live" else f"{base_class} live"
        
        print(f"Current path: {pathname}")
        print(f"Home class: {home_class}")
        
        return home_class, game_class, stats_class, live_class
    
    navbar = html.Div(
        children = [
            # LHS
            html.Div(html.Img(
                src="/assets/images/krueger_chips.png", 
                className="navbar-logo",
                style={"height": "60px", "width": "auto"}
            ), className="navbar-lhs"),

            # RHS
            html.Div([
                html.Div(html.A("Home", href="/", className="navbar-link"), id="home-nav", className="navbar-link-container home"),
                html.Div(html.A("Game", href="/game", className="navbar-link"), id="game-nav", className="navbar-link-container game"),
                html.Div(html.A("Stats", href="/stats", className="navbar-link"), id="stats-nav", className="navbar-link-container stats"),
                html.Div(html.A("Live", href="/live", className="navbar-link"), id="live-nav", className="navbar-link-container live"),
            ], className="navbar-rhs"),
        ],
        className="navbar"
    )
    
    return navbar