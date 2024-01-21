#!/usr/bin/python3

if __name__ == "main":

    import hidden_4 as h

    name = dir(h)

    for name in names:

        if name[:2] != "__":
            print(name)
