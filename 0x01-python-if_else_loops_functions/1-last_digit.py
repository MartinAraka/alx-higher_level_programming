#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    if last == 0:
        print(f"Last digit of {number} is {last} and is {last}")
    else:
        print(f"Last digit of {number} is {last * -1} and is less\
  than 6 and not 0")
    else: 
         if last == 0:
            print(f"Last digit of {number} is {last} and is {last}")
    elif last > 5:
            print(f"Last digit of {number} is {last} and is greater than 5")
    else:
        print(f"Last digit of {number} is {last} and is less than 6 and not 0")
