#!/usr/bin/env python3

"""

Given an integer between 1 and 1000 (1 and 1000 inclusive),
convert the integer into a roman numeral

"""


from collections import OrderedDict


def loop_dict(dictionary, number):
    for key in dictionary:
        if number - key >= 0:
            number -= key
            return dictionary[key], number


def romanizer(number):

    thousands = OrderedDict({1000: "M"})
    hunds = OrderedDict({
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
    })
    tens = OrderedDict({
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
    })
    ones = OrderedDict({
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    })

    output = []
    current = number

    while current > 0:

        if current == 1000:
            output.append(thousands[1000])
            break

        if current >= 100:
            roman, current = loop_dict(hunds, current)
            output.append(roman)

        elif current >= 10:
            roman, current = loop_dict(tens, current)
            output.append(roman)

        else:
            roman, current = loop_dict(ones, current)
            output.append(roman)

    return "".join(output)


if __name__ == "__main__":

    input_count = int(input())

    roman_numerals = []

    for i in range(input_count):
        decimal = int(input())
        roman_numerals.append(romanizer(decimal))

    for i in roman_numerals:
        print(i)
