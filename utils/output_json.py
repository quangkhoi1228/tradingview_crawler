import json
from configs.config import JSON_PATH
from utils.crawler import getAllStockData
from utils.history import getStockHistory
from utils.stock import getStockList


def saveDataToJson(stockInfo, stockHistory):
    stockCode = stockInfo['symbol']
    f = open(f"{JSON_PATH}{stockCode}.json", "w")
    f.write(json.dumps(stockHistory))
    f.close()
    print(f"{stockCode}.json")


def getAllStockToJson():
    getAllStockData(saveDataToJson)
