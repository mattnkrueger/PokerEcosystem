import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, dash_table
import plotly.express as px
import pandas as pd

# custom components
from components.Navbar import Navbar

# import page objects
from pages.Home import HomePage
from pages.Game import GamePage
from pages.Stats import StatsPage
from pages.Live import LivePage

app = dash.Dash(__name__, 
                external_stylesheets=[
                    dbc.themes.BOOTSTRAP,
                    "https://use.fontawesome.com/releases/v5.15.1/css/all.css"
                ],
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
    dcc.Store(id='fullscreen-store', data={'fullscreen': False}),
    
    # Hidden div for body class management
    html.Div(id='body-class-trigger', style={'display': 'none'}),
    
    # Navbar with visibility controlled by fullscreen state
    html.Div(id='navbar-container', children=[Navbar()]),
    
    # Page content
    html.Div(id='page-content', style={
        'padding': '2rem',
        'margin': '1rem',
        'borderRadius': '8px',
        'backgroundColor': 'rgba(255, 255, 255, 0.9)',
    }),
], style={
    'backgroundImage': 'url("/assets/images/cards_background.png")',
    'backgroundSize': 'cover',
    'backgroundPosition': 'center',
    'backgroundRepeat': 'no-repeat',
    'minHeight': '100vh',
})


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

@app.callback(
    [Output('fullscreen-store', 'data'),
     Output('navbar-container', 'style'),
     Output('page-content', 'style'),
     Output('fullscreen-button', 'children')],
    [Input('fullscreen-button', 'n_clicks')],
    [State('fullscreen-store', 'data')]
)
def toggle_fullscreen(n_clicks, fullscreen_data):
    """
    Toggle fullscreen mode when the button is clicked
    """
    if n_clicks is None:
        # Initial load
        return fullscreen_data, None, {
            'padding': '2rem',
            'margin': '1rem',
            'borderRadius': '8px',
            'backgroundColor': 'rgba(255, 255, 255, 0.9)',
        }, html.I(className="fas fa-expand")
    
    # Toggle fullscreen state
    is_fullscreen = not fullscreen_data.get('fullscreen', False)
    fullscreen_data['fullscreen'] = is_fullscreen
    
    if is_fullscreen:
        # Hide navbar and footer
        navbar_style = {'display': 'none'}
        
        # Expand content to fill screen
        content_style = {
            'padding': '3rem',
            'margin': '0',
            'borderRadius': '0',
            'backgroundColor': 'rgba(255, 255, 255, 0.95)',
            'minHeight': '100vh',
            'transition': 'all 0.3s ease',
            'position': 'absolute',
            'top': '0',
            'left': '0',
            'right': '0',
            'bottom': '0',
            'zIndex': '10',
        }
        
        # Change button icon to compress
        button_icon = html.I(className="fas fa-compress")
    else:
        # Show navbar and footer
        navbar_style = {'display': 'block'}
        
        # Normal content size
        content_style = {
            'padding': '2rem',
            'margin': '1rem',
            'borderRadius': '8px',
            'backgroundColor': 'rgba(255, 255, 255, 0.9)',
            'transition': 'all 0.3s ease',
        }
        
        # Change button icon to expand
        button_icon = html.I(className="fas fa-expand")
    
    return fullscreen_data, navbar_style, content_style, button_icon

# Callback to add or remove fullscreen class to the body
app.clientside_callback(
    """
    function(isFullscreen) {
        if(isFullscreen.fullscreen) {
            document.body.classList.add('fullscreen');
        } else {
            document.body.classList.remove('fullscreen');
        }
        return '';
    }
    """,
    Output('body-class-trigger', 'children'),
    [Input('fullscreen-store', 'data')]
)

####################
# ---  RUN APP --- #
####################
if __name__ == '__main__':
    app.run_server(debug=True)
