#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as a paramete """
import sys
from urllib import parse
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = parse.urlencode(email).encode("ascii")
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
