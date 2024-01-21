#!/usr/bin/python3

if  __name__ == "__main__":

    import sys as s

    count = 0
    for i in range(len(s.argv) - 1):
            count += int(s.argv[i + 1])
    print("{}".format(count))
