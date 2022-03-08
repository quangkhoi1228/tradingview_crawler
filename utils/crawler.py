from datetime import datetime
import json
import multiprocessing as mp
from queue import Queue
import queue
import threading
from time import sleep

from configs.config import JSON_PATH, MULTIPLE_THREAD_CONNECTION, SLEEP_CRAWL_TIME

from utils.history import getStockHistory
from utils.stock import getStockList

stockInfoQueue = Queue()


def getStockSymbolData(input):
    while True:
        [handleDataFunction] = input
        stockInfo = stockInfoQueue.get()
        stockCode = stockInfo['symbol']
        stockHistory = getStockHistory(stockCode)
        handleDataFunction(stockInfo, stockHistory)
        sleep(SLEEP_CRAWL_TIME)
        stockInfoQueue.task_done()


def getAllStockData(handleDataFunction):
    startTime = datetime.now()
    stockList = getStockList()
    # stockList = [{"symbol": "AMD"}]

    for i in range(0, MULTIPLE_THREAD_CONNECTION):
        thread = threading.Thread(target=getStockSymbolData,
                                  args=[[handleDataFunction]])
        thread.daemon = True
        thread.start()

    for item in stockList:
        stockInfoQueue.put(item)

    stockInfoQueue.join()
    endTime = datetime.now()
    print(endTime - startTime)
