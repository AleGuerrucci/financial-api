from fastapi import FastAPI, HTTPException
import yfinance as yf

app = FastAPI()

@app.get("/stock")
def get_stock(ticker: str):
    try:
        t = yf.Ticker(ticker)
        data = t.history(period="1d")

        if data.empty:
            raise HTTPException(status_code=404, detail="No data found")

        return {
            "ticker": ticker,
            "price": float(data["Close"].iloc[-1])
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))