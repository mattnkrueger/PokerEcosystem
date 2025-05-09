import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, dash_table
import plotly.express as px
import pandas as pd

# custom components
from components.Navbar import Navbar
from components.Footer import Footer

# import page objects
from pages.Home import HomePage
from pages.Game import GamePage
from pages.Stats import StatsPage
from pages.Live import LivePage

app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                suppress_callback_exceptions=True)
server = app.server  

# Initialize page objects
home_page = HomePage()
game_page = GamePage()
stats_page = StatsPage()
live_page = LivePage()

###################
# ---  LAYOUT --- #
###################
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    Navbar(),
    html.Div(id='page-content'), # main page
    Footer(),
])


#########################
# ---  PAGE OBJECTS --- #
#########################


######################
# ---  CALLBACKS --- #
######################
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    """
    page routing
    """
    if pathname == home_page.path:
        return home_page.layout()
    elif pathname == game_page.path:
        return game_page.layout()
    elif pathname == stats_page.path:
        return stats_page.layout()
    elif pathname == live_page.path:
        return live_page.layout()
    else:
        return html.Div([ html.H1('404 - Page not found') ])

####################
# ---  RUN APP --- #
####################
if __name__ == '__main__':
    app.run_server(debug=True)
