#!/usr/bin/python3
for alpha in range(97, 123):
    letter = chr(alpha)
    if letter not in ('q', 'e'):
        print("{}".format(letter), end="")
