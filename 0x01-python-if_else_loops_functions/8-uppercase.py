#!/usr/bin/python3
def uppercase(s):
    for letter in s:
        upperLetter = chr(ord(letter) - 32) if 'a' <= letter <= 'z' else letter
        print("{}".format(upperLetter), end="")
    print()
