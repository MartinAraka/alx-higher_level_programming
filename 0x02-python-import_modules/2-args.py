#!/usr/bin/python3

if __name__ == "__main__":

    import sys as s

    count = len(s.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, s.argv[i + 1]))
