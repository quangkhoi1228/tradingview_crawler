from cmath import e
from datetime import datetime
import json
import sys
from configs.config import JSON_PATH, POSTGRESQL_DELETE_YEAR_DATA_QUERY_BUILDER, POSTGRESQL_INFO, POSTGRESQL_INSERT_QUERY_BUILDER, POSTGRESQl_PATH, POSTGRESQl_TABLE
from utils.crawler import getAllStockData, getAllStockDataCurrentYear
from utils.helper import clearFolder, getFileInPath, writeFile
from utils.history import getStockHistory
from utils.stock import getStockList
import psycopg2


def saveDataToPosgresql(stockInfo, stockHistory):
    stockCode = stockInfo['symbol']
    # stockHistory = [stockHistory[0]]
    query = ''
    for stockHistoryItem in stockHistory:
        query = query + POSTGRESQL_INSERT_QUERY_BUILDER(
            stockCode, stockInfo['type'], datetime.utcfromtimestamp(stockHistoryItem['time']), stockHistoryItem['open'], stockHistoryItem['close'], stockHistoryItem['high'], stockHistoryItem['low'], stockHistoryItem['volume']) + ''';
'''
    excuteQuery(query)
    writeFile(f"{POSTGRESQl_PATH}{stockCode}.sql", query)
    print(f"{stockCode}.sql {len(stockHistory)} item")


def excuteQuery(query):
    connection = psycopg2.connect(
        host=POSTGRESQL_INFO["host"],
        database=POSTGRESQL_INFO["database"],
        user=POSTGRESQL_INFO["user"],
        password=POSTGRESQL_INFO["password"])
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


def getAllStockToPostgresql():
    clearFolder(POSTGRESQl_PATH)
    excuteQuery(f"truncate {POSTGRESQl_TABLE}")
    getAllStockData(saveDataToPosgresql)


def saveDataToPosgresqlCurrentYear(stockInfo, stockHistory):
    year = datetime.now().year
    clearCurrentYearDataQuery = POSTGRESQL_DELETE_YEAR_DATA_QUERY_BUILDER(
        stockInfo['symbol'], year)
    excuteQuery(clearCurrentYearDataQuery)
    saveDataToPosgresql(stockInfo, stockHistory)


def getTodayAllStockToPostgresql():
    clearFolder(POSTGRESQl_PATH)
    getAllStockDataCurrentYear(saveDataToPosgresqlCurrentYear)
    print(len(getFileInPath(POSTGRESQl_PATH)))
