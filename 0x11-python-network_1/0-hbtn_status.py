#!/usr/bin/python3
""" Fetch a url """

if __name__ == "__main__":
    from urllib import request
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        data = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode('utf-8')))
