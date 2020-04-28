#!/usr/bin/python3
for tens in range(0, 10):
    for ones in range(tens, 10):
        if tens != ones:
            print("{:d}".format(tens), end="")
            if tens != 8:
                print("{:d}".format(ones), end=", ")
            else:
                print("{:d}".format(ones))
