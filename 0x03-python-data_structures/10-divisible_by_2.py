#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    result = []

    for num in my_list:

        divisible = num % 2 == 0

        result.append(divisible)

    return result
