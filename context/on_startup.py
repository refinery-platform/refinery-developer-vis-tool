from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import requests

if __name__ =="__main__":
    # input.json should just be in place already, if it has been given.
    # Using environ.get to be a little more robust against missing values.

    with open("envvar_value.json", "w") as f:
        f.write(
            os.environ.get("INPUT_JSON")
        )

    with open("envvar_url.json", "w") as f:
        f.write(
            requests.get(os.environ.get("INPUT_JSON_URL")).text
        )

    HTTPServer(('', 80), SimpleHTTPRequestHandler).serve_forever()