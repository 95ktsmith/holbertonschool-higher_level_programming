#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {}".format(number), end=" ")

if number < 0:
    digit = ((number * -1) % 10) * -1
else:
    digit = number % 10
print("is {}".format(digit), end=" ")

if digit > 5:
    print("and is greater than 5")
elif digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
