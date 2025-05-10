import dash_bootstrap_components as dbc
from dash import html

class StatsPreview:
    def __init__(self):
        self.name = "StatsPreview"
    
    def layout(self):
        return html.Div([
            html.H3("Quick Stats", className="h4 mb-3"),
            
            # Top Winners Section
            html.Div([
                html.H4("Top Winners", className="h6 mb-2"),
                html.Div([
                    html.Div([
                        html.Span("1. Player 1", className="me-2", style={"fontSize": "0.9rem"}),
                        html.Span("+$500", className="text-success", style={"fontSize": "0.9rem"})
                    ], className="mb-1"),
                    html.Div([
                        html.Span("2. Player 2", className="me-2", style={"fontSize": "0.9rem"}),
                        html.Span("+$300", className="text-success", style={"fontSize": "0.9rem"})
                    ], className="mb-1"),
                    html.Div([
                        html.Span("3. Player 3", className="me-2", style={"fontSize": "0.9rem"}),
                        html.Span("+$200", className="text-success", style={"fontSize": "0.9rem"})
                    ], className="mb-1"),
                ], className="mb-3")
            ]),
            
            # Largest Hands Section
            html.Div([
                html.H4("Largest Hands", className="h6 mb-2"),
                html.Div([
                    html.Div([
                        html.Span("Biggest Win:", className="me-2", style={"fontSize": "0.9rem"}),
                        html.Span("$1,200", className="text-success", style={"fontSize": "0.9rem"})
                    ], className="mb-1"),
                    html.Div([
                        html.Span("Biggest Loss:", className="me-2", style={"fontSize": "0.9rem"}),
                        html.Span("$800", className="text-danger", style={"fontSize": "0.9rem"})
                    ], className="mb-1"),
                ])
            ])
        ], className="stats-preview p-3 bg-light rounded shadow-sm") 