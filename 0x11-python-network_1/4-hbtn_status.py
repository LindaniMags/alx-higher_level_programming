#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status. """
import requests

url = "https://alx-intranet.hbtn.io/status"
response = requests.get(url)

print("Body response:")
print(f"\t- type: {type(response.text)}")
print(f"\t- content: {response.text}")
