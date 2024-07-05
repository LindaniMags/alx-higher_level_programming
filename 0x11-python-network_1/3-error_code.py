#!/usr/bin/python3
""" Manages errors and displays the url body """

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
