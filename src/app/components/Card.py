import dash
from dash import html
import dash_bootstrap_components as dbc

def Card(icon, title, description, button_text, button_href):
    return dbc.Card(
        [
            html.Div(
                icon,
                className="card-icon",
                style={"textAlign": "center", "marginTop": "4px", "marginBottom": "0"}
            ),
            dbc.CardBody([
                html.H4(title, className="card-title", style={"textAlign": "center", "fontSize": "1rem", "marginBottom": "4px", "marginTop": "6px"}),
                html.P(description, className="card-description", style={"textAlign": "center", "fontSize": "0.8rem", "marginBottom": "8px"}),
                dbc.Button(
                    button_text,
                    href=button_href,
                    color="primary",
                    className="card-btn",
                    style={"marginTop": "4px", "display": "block", "marginLeft": "auto", "marginRight": "auto", "fontSize": "0.8rem", "padding": "6px 16px"}
                )
            ])
        ],
        className="custom-card",
        style={
            "width": "100%",
            "maxWidth": "220px",
            "minHeight": "120px",
            "boxShadow": "0 2px 12px 0 rgba(60,60,60,0.08)",
            "borderRadius": "8px",
            "padding": "0",
            "margin": "4px auto"
        }
    ) 