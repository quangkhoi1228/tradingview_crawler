import json
import multiprocessing as mp
from queue import Queue
import queue
import threading

from configs.config import JSON_PATH, MULTIPLE_THREAD_CONNECTION

from utils.history import getStockHistory
from utils.stock import getStockList

stockInfoQueue = Queue()


def getStockSymbolData(input):
    while True:
        [handleDataFunction] = input
        stockInfo = stockInfoQueue.get()
        print(stockInfo)
        stockCode = stockInfo['symbol']
        stockHistory = getStockHistory(stockCode)
        handleDataFunction(stockInfo, stockHistory)
        stockInfoQueue.task_done()


def getAllStockData(handleDataFunction):
    stockList = getStockList()

    for i in range(0, MULTIPLE_THREAD_CONNECTION):
        thread = threading.Thread(target=getStockSymbolData,
                                  args=[[handleDataFunction]])
        thread.daemon = True
        thread.start()

    for item in stockList:
        stockInfoQueue.put(item)

    stockInfoQueue.join()
