#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    result = 0
    previous = 0
    for char in reversed(roman_string):
        value = roman_numerals.get(char, 0)
        if value >= previous:
            result += value
        else:
            result -= value
        previous = value
    return result
