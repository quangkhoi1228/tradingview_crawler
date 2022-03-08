import json
from configs.config import JSON_PATH
from utils.crawler import getAllStockData
from utils.helper import writeFile
from utils.history import getStockHistory
from utils.stock import getStockList


def saveDataToJson(stockInfo, stockHistory):
    stockCode = stockInfo['symbol']
    writeFile(f"{JSON_PATH}{stockCode}.json", json.dumps(stockHistory))
    print(f"{stockCode}.json {len(stockHistory)} item")


def getAllStockToJson():
    getAllStockData(saveDataToJson)
