#!/usr/local/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    while True:
        try:
            if count < x:
                print(my_list[count], end='')
                count += 1
            else:
                print()
                return count
            except IndexError:
                print()
                return count
