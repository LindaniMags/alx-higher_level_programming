#!/usr/bin/python3
""" Evaluates candidates applying for a back-end position """
import sys
import requests

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    response = requests.get(url)
    c = response.json()
    try:
        for i in range(10):
            print(f"{c[i].get("sha")}: {c[i].get("commit").get("author").get("name")}")
    except IndexError:
        pass
