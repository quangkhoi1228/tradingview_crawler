from datetime import datetime
import os
from tkinter import MULTIPLE


DATA_URL = 'https://dchart-api.vndirect.com.vn/dchart'

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# ALPHABET = ['A']
INTERVAL = "D"

MULTIPLE_THREAD_CONNECTION = 15
SLEEP_CRAWL_TIME = 1.5

CSV_PATH = f'{os.getcwd()}/out/csv/'
JSON_PATH = f'{os.getcwd()}/out/json/'
SQL_PATH = f'{os.getcwd()}/out/sql/'
POSTGRESQl_PATH = f'{os.getcwd()}/out/postgresql/'


POSTGRESQL_INFO = {
    "host": "10.78.28.51",
    "database": "dbpugna",
    "user": "gbsofts",
    "password": ""
}


def POSTGRESQL_INSERT_QUERY_BUILDER(stockCode, stockType, tradingDate, open, close, high, low, volume):
    user = 'system'
    date = datetime.now()
    return f'''INSERT INTO tbstockchart(symbolname, symboltype, tradingdate, "open", "close", high, low, volume, createddate, createduser, lastmodifieddate, lastmodifieduser) VALUES('{stockCode}', '{stockType}', '{tradingDate}', {open}, {close}, {high}, {low}, {volume},  '{date}','{user}',  '{date}','{user}')'''
