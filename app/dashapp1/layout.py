import dash_core_components as dcc
import dash_html_components as html

layout = html.Div([
    html.A('Home', href='/'),
    html.H1('Stock Tickers'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Amazon', 'value': 'AMZN'},
            {'label': 'Apple', 'value': 'AAPL'},
            {'label': 'Black Rock', 'value': 'BLK'},
            {'label': 'Disney', 'value': 'DIS'},
            {'label': 'Procter & Gamble', 'value': 'PG'},
            {'label': 'United Health Group', 'value': 'UNH'},
        ],
        value='UNH'
    ),
    dcc.Graph(id='my-graph')
], style={'width': '500'})
