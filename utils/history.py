from datetime import datetime
import json
from numpy import append
import requests

from configs.config import DATA_URL, INTERVAL


def getStockHistory(stockCode):
    nextYear = datetime.now().year + 1
    result = []

    for year in reversed(range(2000, nextYear)):
        stockHistory = getStockHistoryInYear(stockCode, year)
        if(len(stockHistory) == 0):
            return result
        result.extend(stockHistory)
    return result


def getStockHistoryCurrentYear(stockCode):
    return getStockHistoryInYear(stockCode, datetime.now().year)


def getStockHistoryInYear(stockCode, year):
    startDay = round(datetime.timestamp(datetime(year, 1, 1)))
    endDay = round(datetime.timestamp(datetime(year, 12, 31)))

    url = f"{DATA_URL}/history?resolution={INTERVAL}&symbol={stockCode}&from={startDay}&to={endDay}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    historyList = []
    try:
        stockHistoryInfo = json.loads(response.text)

        open = stockHistoryInfo['o']
        high = stockHistoryInfo['h']
        low = stockHistoryInfo['l']
        close = stockHistoryInfo['c']
        volume = stockHistoryInfo['v']
        time = stockHistoryInfo['t']
        for index in range(len(open)):
            historyList.append({
                "symbol": stockCode,
                "open": open[index],
                "high": high[index],
                "low": low[index],
                "close": close[index],
                "volume": volume[index],
                "time": time[index],

            })
    except:
        print(url)
    finally:
        # print(f"No data{stockCode} {year}")
        # print(f"crawl {stockCode} {year}: {len(historyList)} item")

        return historyList
