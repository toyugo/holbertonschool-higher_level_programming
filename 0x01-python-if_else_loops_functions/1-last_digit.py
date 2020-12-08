#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
td = ["and is greater than 5", "and is 0", "and is less than 6 and not 0"]
index = 0
if number < 0:
    number1 = number * -1
else:
    number1 = number
lastdigit = number1 % 10
if lastdigit > 5:
    index = 0
elif lastdigit == 0:
    index = 1
elif lastdigit < 6:
    index = 2
print("Last digit of {0} is {1} {2}".format(number, lastdigit, td[index]))
