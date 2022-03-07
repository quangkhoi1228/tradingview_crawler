from datetime import datetime
from sqlite3 import Timestamp
import requests

from configs.config import DATA_URL, INTERVAL


def getStockHistory(stockCode):
    nextYear = datetime.now().year + 1
    for year in range(2000, nextYear):
        getStockHistoryInYear(stockCode, year)


def getStockHistoryInYear(stockCode, year):
    startDay = round(datetime.timestamp(datetime(year, 1, 1)))
    endDay = round(datetime.timestamp(datetime(year, 12, 31)))

    url = f"{DATA_URL}/history?resolution={INTERVAL}&symbol={stockCode}&from={startDay}&to={endDay}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
