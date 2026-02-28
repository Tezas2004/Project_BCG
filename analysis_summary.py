"""
Financial data analysis summary (Task 1 context).
Run this to refresh the numbers used by the chatbot responses.
"""
import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent / "financial_data.csv"

def load_and_analyze():
    df = pd.read_csv(DATA_PATH)
    df["year"] = df["year"].astype(int)
    latest = df.iloc[-1]
    prior = df.iloc[-2]
    return {
        "total_revenue_latest": latest["revenue"],
        "total_revenue_prior": prior["revenue"],
        "net_income_latest": latest["net_income"],
        "net_income_prior": prior["net_income"],
        "net_income_change_pct": round(
            (latest["net_income"] - prior["net_income"]) / prior["net_income"] * 100, 1
        ),
        "revenue_change_pct": round(
            (latest["revenue"] - prior["revenue"]) / prior["revenue"] * 100, 1
        ),
        "operating_expenses_latest": latest["operating_expenses"],
        "total_assets_latest": latest["total_assets"],
        "years": list(df["year"]),
    }

if __name__ == "__main__":
    summary = load_and_analyze()
    for k, v in summary.items():
        print(f"{k}: {v}")
