import requests
import pandas as pd
from datetime import datetime

def fetch_ohlc(symbol="PI_XBTUSD", interval=1):
    url = "https://futures.kraken.com/derivatives/api/v3/history"

    params = {
        "symbol": symbol,
        "interval": interval
    }

    response = requests.get(url, params=params)
    data = response.json()

    candles = data.get("candles", [])

    rows = []
    for c in candles:
        timestamp = datetime.utcfromtimestamp(c["time"] / 1000)
        open_price = float(c["open"])
        high = float(c["high"])
        low = float(c["low"])
        close = float(c["close"])
        volume = float(c["volume"])

        rows.append([timestamp, open_price, high, low, close, volume])

    df = pd.DataFrame(rows, columns=["timestamp", "open", "high", "low", "close", "volume"])
    return df


def main():
    df = fetch_ohlc()

    print("Data Loaded:")
    print(df.tail())


if __name__ == "__main__":
    main()
