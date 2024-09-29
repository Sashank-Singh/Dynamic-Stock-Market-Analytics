
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from data_processing import fetch_stock_data, calculate_returns
from visualization import create_return_chart

print("Initializing Dash app...")

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # For deployment

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Dynamic Stock Market Analytics",
                        className='text-center text-primary mb-4'),
                width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Input(id='ticker-input', placeholder='Enter Stock Ticker (e.g., AAPL)', type='text', value='AAPL'),
        ], width=8),
        dbc.Col([
            dbc.Button('Submit', id='submit-button', color='primary')
        ], width=4),
    ], className='mb-4'),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='return-chart')
        ], width=12)
    ])
], fluid=True)

@app.callback(
    Output('return-chart', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('ticker-input', 'value')]
)
def update_chart(n_clicks, ticker):
    print(f"Callback triggered with ticker: {ticker}")
    if not ticker:
        ticker = 'AAPL'  # Default ticker

    df = fetch_stock_data(ticker)
    if df.empty:
        print(f"No data found for ticker: {ticker}")
        return {
            'data': [],
            'layout': {
                'title': f"No data found for ticker: {ticker}",
                'xaxis': {'visible': False},
                'yaxis': {'visible': False}
            }
        }

    df = calculate_returns(df)
    fig = create_return_chart(df, ticker.upper())
    print(f"Chart created for ticker: {ticker.upper()}")
    return fig

if __name__ == '__main__':
    print("Starting Dash server...")
    app.run_server(debug=True)

