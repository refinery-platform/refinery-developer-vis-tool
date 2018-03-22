from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import requests

if __name__ =="__main__":
    # input.json should just be in place already, if it has been given.

    # If you're using this as template to start from, you probably don't care
    # which mode was used, and every case should write to the same input.json.

    json = os.environ.get("INPUT_JSON")
    if json:
        with open("envvar_value.json", "w") as f:
            f.write(json)

    url = os.environ.get("INPUT_JSON_URL")
    if url:
        with open("envvar_url.json", "w") as f:
            f.write(requests.get(url).text)

    print('envvars read')

    HTTPServer(('', 80), SimpleHTTPRequestHandler).serve_forever()

    print('server started')