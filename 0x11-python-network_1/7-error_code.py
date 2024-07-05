#!/usr/bin/python3
""" If the HTTP status code is greater than or equal to 400, print: Error code """
import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(argv[1])
    status = response.status_code
    if (status < 400):
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))
