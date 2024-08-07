#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as a parameter """
import requests
from sys import argv

if __name__ == '__main__':
    payload = {'email': argv[2]}
    response = requests.post(argv[1], data=payload)
    print(response.text)
