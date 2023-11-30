#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = len(argv)

    result = 0

    for i in range(1, count):
        result += int(argv[i])
    print("{:d}".format(result))
