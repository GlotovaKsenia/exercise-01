import csv
from pathlib import Path
from typing import Any
import pandas as pd

CSV_PATH = Path(__file__).parent / "assortment.csv"


def gross_price(net_price: float, tax_rate: float) -> float:
    return round(net_price * (1 + tax_rate), 2)


def load_catalogue(path: Path = CSV_PATH) -> dict[int, dict[str, Any]]:
    """Baut aus einer CSV-Datei ein Dictionary im Aufbau von CATALOGUE"""
    catalogue: dict[int, dict[str, Any]] = {}
    with open(path, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            catalogue[int(row["number"])] = {
                "name": row["name"],
                "group": row["group"],
                "subgroup": row["subgroup"] or None,
                "net_price": float(row["net_price"]),
                "tax_rate": float(row["tax_rate"]),
                "stock": int(row["stock"]),
            }
    return catalogue

def daily_report(path: Path = CSV_PATH) -> pd.Series:
    frame = pd.read_csv(path)
    gross = pd.Series(frame["net_price"]*(1+frame["tax_rate"]), dtype=float)

    frame["gross_price"]=gross.round(2)
    stock_value = pd.Series(frame["gross_price"]*frame["stock"], dtype=float)

    frame["stock_value"] = stock_value.round(2)
    totals = frame.groupby("group")["stock_value"].sum()
    report = pd.Series(totals, dtype=float).round(2)

    report["Summe"] = round(float(report.sum()), 2)
    return report


if __name__ == "__main__":
    for number, article in load_catalogue().items():
        gross = gross_price(article["net_price"], article["tax_rate"])
        print(number, article["name"], gross, "Euro")
    print(daily_report())
