#!/usr/bin/python3
for twoDigs in range(10):
    for oneDig in range(twoDigs + 1, 10):
        if twoDigs == 8 and oneDig == 9:
            print("{}{}".format(twoDigs, oneDig))
        else:
            print("{}{}".format(twoDigs, oneDig), end=", ")
