import requests

def handler(request):
    url = "https://futures.kraken.com/derivatives/api/v3/history/executions"
    params = {
        "symbol": "PI_XBTUSD"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return {
        "statusCode": 200,
        "body": data
    }
