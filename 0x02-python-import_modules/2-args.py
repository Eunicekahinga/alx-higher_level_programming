#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    count = len(argv) -1

    if count == 0:
        print("{}".format("0 arguments."))
    elif count == 1:
        print("{}".format("1 argument:"))
        print("1: {}".format(argv[1]))
    else:
        print("{:d} {}".format(count, "arguments:"))
        for i in range(1, count + 1):
            print("{:d}: {}".format(i, argv[i]))
