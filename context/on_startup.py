from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import json
import requests

if __name__ =="__main__":
    with open("input.json", "w") as f:
        f.write(
            json.dumps(
                requests.get(os.environ["INPUT_JSON_URL"]).json()
            )
        )

    HTTPServer(('', 80), SimpleHTTPRequestHandler).serve_forever()