#!/usr/bin/python3
""" Sends a request to the URL and displays the value of the X-Request-Id  """
import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]

    req = request.Request(url)
    with request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
