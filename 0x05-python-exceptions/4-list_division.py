#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list = []
    try:
        for i in range(list_length):
            try:
                list.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                print("Division by 0")
                list.append(0)
            except IndexError:
                print("Out of range")
                list.append(0)
            except (TypeError, ValueError):
                print("Wrong type")
                list.append(0)
    finally:
        return list
