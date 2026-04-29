from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/stock")
def get_stock(ticker: str):
    t = yf.Ticker(ticker)
    info = t.info

    return {
        "ticker": ticker,
        "price": info.get("regularMarketPrice"),
        "marketCap": info.get("marketCap"),
        "currency": info.get("currency")
    }