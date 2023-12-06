#!/usr/bin/python3

def uniq_add(my_list=[]):

    uniq = 0
    for num in set(my_list):
        uniq += num
    return (uniq)
