#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    last_digit = number % 10
elif number < 0:
    last_digit = -(number) % 10
else:
    last_digit = number

if number > 5:
    print(
        f"Last digit of {number} is {last_digit} and is greater than 5")
elif number == 0:
    print(f"Last digit of {number} is {number} and is 0")
else:
    print(
        f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
