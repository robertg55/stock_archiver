from fetcher import StockTracker

if __name__ == "__main__":
    data = {"SQQQ": None, "TQQQ": None, "SPY": None}

    for symbol in data.keys():
        t = StockTracker(symbol, data)
        t.start()
