'''
    Simple python project that tracks the top 5 trending stocks.
'''
import requests
import json


# #define url and api keys and tickers
api = "B2R3RJ0M9CYKA0NG"
# URL = "https://www.alphavantage.co/query?"
tickers = ["ibm", "goog"]
# # sets the function to pass into the api
apiFunc = ["TIME_SERIES_INTRADAY"]


response_API = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+ tickers[1] +'&interval=5min&apikey=' + api)
print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
info = parse_json['Meta Data']
print("Info about API:\n", info)