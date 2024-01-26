#!/usr/bin/python3

def uniq_add(my_list=[]):

    result = set(my_list)
    sum = 0
    for i in result:
        sum += int(i)
    return (sum)
