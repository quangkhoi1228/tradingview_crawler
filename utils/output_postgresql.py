from cmath import e
from datetime import datetime
import json
import sys
from configs.config import JSON_PATH, POSTGRESQL_INFO, POSTGRESQL_INSERT_QUERY_BUILDER, POSTGRESQl_PATH
from utils.crawler import getAllStockData
from utils.history import getStockHistory
from utils.stock import getStockList
import psycopg2


def saveDataToPosgresql(stockInfo, stockHistory):
    stockCode = stockInfo['symbol']
    # stockHistory = [stockHistory[0]]
    query = ''
    for stockHistoryItem in stockHistory:
        query = query + POSTGRESQL_INSERT_QUERY_BUILDER(
            stockCode, stockInfo['type'], datetime.utcfromtimestamp(stockHistoryItem['time']), stockHistoryItem['open'], stockHistoryItem['close'], stockHistoryItem['high'], stockHistoryItem['low'], stockHistoryItem['volume']) + ';'

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

    f = open(f"{POSTGRESQl_PATH}{stockCode}.sql", "w")
    f.write(query)
    f.close()
    print(f"{stockCode}.sql {len(stockHistory)} item")


def getAllStockToPostgresql():
    getAllStockData(saveDataToPosgresql)
