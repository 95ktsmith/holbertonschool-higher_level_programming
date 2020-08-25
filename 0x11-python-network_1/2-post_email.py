#!/usr/bin/python3
""" POST an email """

if __name__ == "__main__":
    from urllib import request
    from urllib import parse
    from sys import argv
    data = parse.urlencode({'email': argv[2]}).encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
