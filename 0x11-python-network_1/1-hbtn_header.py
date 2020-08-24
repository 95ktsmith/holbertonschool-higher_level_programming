#!/usr/bin/python3
""" Get request ID """

if __name__ == "__main__":
    from urllib import request
    from sys import argv
    with request.urlopen(argv[1]) as response:
        print(response.info()['X-Request-Id'])
