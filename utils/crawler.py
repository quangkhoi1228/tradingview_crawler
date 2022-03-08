from datetime import datetime
import json
import multiprocessing as mp
from queue import Queue
import queue
import threading
from time import sleep

from configs.config import JSON_PATH, MULTIPLE_THREAD_CONNECTION, SLEEP_CRAWL_TIME

from utils.history import getStockHistory, getStockHistoryCurrentYear
from utils.stock import getStockList

stockInfoQueue = Queue()


def getStockSymbolDataProcess(input, getStockHistoryFunction, delayTime):
    while True:
        [handleDataFunction] = input
        stockInfo = stockInfoQueue.get()
        stockCode = stockInfo['symbol']
        stockHistory = getStockHistoryFunction(stockCode)
        handleDataFunction(stockInfo, stockHistory)
        sleep(delayTime)
        stockInfoQueue.task_done()


def getStockSymbolData(input):
    getStockSymbolDataProcess(input, getStockHistory, SLEEP_CRAWL_TIME)


def getStockSymbolDataCurrentYear(input):
    getStockSymbolDataProcess(
        input, getStockHistoryCurrentYear, SLEEP_CRAWL_TIME / 5)


def getAllStockDataProcess(getStockSymbolFunction, handleDataFunction):
    startTime = datetime.now()
    stockList = getStockList()
    # stockList = [{"symbol": "AMD"}]

    for i in range(0, MULTIPLE_THREAD_CONNECTION):
        thread = threading.Thread(target=getStockSymbolFunction,
                                  args=[[handleDataFunction]])
        thread.daemon = True
        thread.start()

    for item in stockList:
        stockInfoQueue.put(item)

    stockInfoQueue.join()

    endTime = datetime.now()
    print(endTime - startTime, f"stock list: {len(stockList)}")


def getAllStockData(handleDataFunction):
    getAllStockDataProcess(getStockSymbolData, handleDataFunction)


def getAllStockDataCurrentYear(handleDataFunction):
    getAllStockDataProcess(getStockSymbolDataCurrentYear, handleDataFunction)
