#!/usr/bin/python3
""" Get ID Header """

if __name__ == "__main__":
    import requests
    from sys import argv
    print(requests.get(argv[1]).headers['X-Request-Id'])
