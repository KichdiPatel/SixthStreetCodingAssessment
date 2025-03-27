import requests
import pandas as pd


class AlphaVantage:
    def __init__(self, api_key):
        """
        Initialize the AlphaVantage object with an API key
        """
        self.api_key = api_key

    def _fetch_daily_series(self, symbol: str):
        """
        Internal helper to fetch TIME_SERIES_DAILY data from Alpha Vantage.
        """
        api = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize={"full"}&apikey={self.api_key}"
        try: 
            response = requests.get(api)
            response.raise_for_status()
            data = response.json()
            time_series = data["Time Series (Daily)"]

            df = pd.DataFrame.from_dict(time_series, orient="index")
            df.rename(columns={
                "1. open": "open",
                "2. high": "high",
                "3. low": "low",
                "4. close": "close",
                "5. volume": "volume"
            }, inplace=True)
            df.index = pd.to_datetime(df.index)
            df.sort_index(ascending=False, inplace=True)
            df = df.astype({
                "open": float,
                "high": float,
                "low": float,
                "close": float,
                "volume": int
            })
            df.reset_index(inplace=True)
            df.rename(columns={"index": "date"}, inplace=True)
            return df
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
        
    def lookup(self, symbol: str, date: str):
        """
        given a symbol and a date, return the open, high, low, close, 
        and volume for that symbol on that date.

        Args:
            symbol (str): The stock ticker symbol (e.g., "AAPL").
            date (str): The date in "YYYY-MM-DD" format.

        Returns:
            dict or None: The OHLCV data if found, otherwise None.
        """

        df = self._fetch_daily_series(symbol)
        if df is None:
            return None

        found = df[df["date"] == pd.to_datetime(date)]
        if found.empty:
            print(f"No data found for {symbol} on {date}")
            return None
        else:
            row = found.iloc[0]
            return {
                "open": float(row["open"]),
                "high": float(row["high"]),
                "low": float(row["low"]),
                "close": float(row["close"]),
                "volume": int(row["volume"])
            }   

    def min(self, symbol: str, n: int):
        """
        given a symbol and a range 'n', return the lowest price 
        that symbol traded at over the last 'n' data points (lowest low)

        Args:
            symbol (str): The stock ticker symbol.
            n (int): Number of most recent trading days to consider.

        Returns:
            float or None: The lowest low value, or None if not available.
        """

        df = self._fetch_daily_series(symbol)
        if df is None or len(df) < n:
            print(f"Not enough data to compute min for {symbol} over last {n} days.")
            return None
        else:
            return df.head(n)["low"].min()

    def max(self, symbol: str, n: int):
        """
        given a symbol and a range 'n', return the highest price that symbol 
        traded at over the last 'n' data points (highest high)

        Args:
            symbol (str): The stock ticker symbol.
            n (int): Number of most recent trading days to consider.

        Returns:
            float or None: The highest high value, or None if not available.
        """
        df = self._fetch_daily_series(symbol)
        if df is None or len(df) < n:
            print(f"Not enough data to compute max for {symbol} over last {n} days.")
            return None

        return df.head(n)["high"].max()

# if __name__ == "__main__":
#     av = AlphaVantage("demo")
#     # print(av.lookup("AAPL", "2025-03-25"))
#     # df = av._fetch_daily_series("MSFT")
#     # print("Oldest date available:", df["date"].min())
#     # print("Newest date available:", df["date"].max())


# #     data1 = av.lookup("AAPL", "2025-03-26")
#     print(av.lookup("MSFT", "2025-03-25"))
#     print(av.min("MSFT", 5))
#     print(av.max("MSFT", 5))
#     data2 = av.min("AAPL", 5)
#     print(data2)
#     data3 = av.max("AAPL", 5)
#     print(data3)