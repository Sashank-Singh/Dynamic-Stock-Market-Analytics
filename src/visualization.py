import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd

def create_return_chart(df: pd.DataFrame, ticker: str) -> go.Figure:
    """
    Creates an interactive chart for daily and cumulative returns.

    :param df: DataFrame with stock data and returns
    :param ticker: Stock ticker symbol
    :return: Plotly Figure object
    """
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        subplot_titles=(f"{ticker} Daily Returns", f"{ticker} Cumulative Returns"))

    # Daily Return
    fig.add_trace(go.Bar(x=df['Date'], y=df['Daily Return'],
                         name='Daily Return',
                         marker_color='indianred'), row=1, col=1)

    # Cumulative Return
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Cumulative Return'],
                             mode='lines',
                             name='Cumulative Return',
                             line=dict(color='green')), row=2, col=1)

    fig.update_layout(height=700, title_text=f"{ticker} Stock Return Analysis",
                      showlegend=False)

    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Daily Return", row=1, col=1)
    fig.update_yaxes(title_text="Cumulative Return", row=2, col=1)

    return fig

