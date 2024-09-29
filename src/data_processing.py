import pandas as pd
import yfinance as yf

def fetch_stock_data(ticker: str, period: str = "1mo", interval: str = "1d") -> pd.DataFrame:
    """
    Fetches historical stock data for a given ticker.

    :param ticker: Stock ticker symbol (e.g., 'AAPL')
    :param period: Data period (e.g., '1mo', '6mo', '1y')
    :param interval: Data interval (e.g., '1d', '1h')
    :return: DataFrame containing stock data
    """
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)
    df.reset_index(inplace=True)
    return df

def calculate_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates daily and cumulative returns.

    :param df: DataFrame with stock data
    :return: DataFrame with added return columns
    """
    df['Daily Return'] = df['Close'].pct_change()
    df['Cumulative Return'] = (1 + df['Daily Return']).cumprod() - 1
    return df
