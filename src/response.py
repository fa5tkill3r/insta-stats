# To authenticate request
from src.credentials import getHeaders, getUserID

# To contact Instagram's API
import requests

# To parse JSON parameters
import json
import urllib


HEADERS = getHeaders()
USER_ID = getUserID()


def makeRequest(option):
    data = []
    after = None
    hasNext = True

    while hasNext:
        PARAMS = {
            "query_hash": option['hash'],
            "variables": json.dumps({
                "id": USER_ID,
                "include_reel": True,
                "fetch_mutual": True,
                "first": 50,
                "after": after
            })
        }
        URL = "https://www.instagram.com/graphql/query/?" + urllib.parse.urlencode(PARAMS)

        response = requests.get(url=URL, headers=HEADERS).json()
        hasNext = response['data']['user'][option['path']]['page_info']['has_next_page']
        after = response['data']['user'][option['path']]['page_info']['end_cursor']
        data += response['data']['user'][option['path']]['edges']

    return data
