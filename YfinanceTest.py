import yfinance as yf

data = yf.download("EURUSD=X", start="2022-01-01", interval="1h")

print(data.info())