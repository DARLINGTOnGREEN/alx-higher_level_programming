#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    sign = -1
else:
    sign = 1
last_digit = abs(number) % 10 * sign
print(f"Last digit of {number} is {last_digit} and is", end=" ")
if number > 5:
    print("greater than 5")
elif number == 0:
    print("0")
elif number < 6 and number != 0:
    print("less than 6 and not 0")
