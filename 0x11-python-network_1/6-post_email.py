#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as a parameter """
import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]
    request = request.Request(url)
    with request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
