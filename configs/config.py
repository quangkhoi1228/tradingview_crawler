import os
from tkinter import MULTIPLE


DATA_URL = 'https://dchart-api.vndirect.com.vn/dchart'

# ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
# 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ALPHABET = ['A', 'B']
INTERVAL = "D"

MULTIPLE_THREAD_CONNECTION = 100

CSV_PATH = f'{os.getcwd()}/out/csv/'
JSON_PATH = f'{os.getcwd()}/out/json/'
SQL_PATH = f'{os.getcwd()}/out/sql/'
