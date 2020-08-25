#!/usr/bin/python3
""" Print error code """

if __name__ == "__main__":
    from urllib import request
    from urllib import error
    from sys import argv
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
