from configs.config import ALPHABET, DATA_URL
import requests
import json


def getStockList():
    listAllStockInfo = []
    for character in ALPHABET:
        listStockInfoByCharacter = getStockListByCharacter(character)
        listAllStockInfo.extend(listStockInfoByCharacter)
        return listAllStockInfo


def getStockListByCharacter(character):
    print(f'crawl symbol begin with {character} character')
    url = f"{DATA_URL}/search?limit=3000&query={character}&type=&exchange="
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    listStockInfo = json.loads(response.text)
    return reversed(listStockInfo)
