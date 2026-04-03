from http.server import BaseHTTPRequestHandler
import json
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = "https://futures.kraken.com/derivatives/api/v3/history/executions"
        params = {
            "symbol": "PI_XBTUSD"
        }

        response = requests.get(url, params=params)
        data = response.json()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        self.wfile.write(json.dumps(data).encode())

