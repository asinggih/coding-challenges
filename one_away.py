#!/usr/bin/env python3
#
# Written by asinggih 05/03/19

"""
---------------------------------------
             Problem set
---------------------------------------
There are three types of edits that can be performed on strings:
    - insert a character
    - remove a character
    - or replace a character

Given two strings, write a function to check if they are
one edit (or zero edits) away.
"""


def one_away(string_A, string_B):
    """
    A function to check if the two given strings are one edit away to
    be an exact match
    """

    # check if it's the same string
    if string_A == string_B:
        return True

    # if string length difference is more than 1, it cannot be right
    if abs(len(string_A)-len(string_B)) > 1:
        return False

    # find which string is longer or shorter, to make it easier later on
    if len(string_A) >= len(string_B):
        longer = string_A
        shorter = string_B
    else:
        longer = string_B
        shorter = string_A

    # indexes for loops
    i = 0
    j = 0

    edits = 0        # keeping track of edits needed

    while i < len(shorter):

        if longer[i] != shorter[j]:
            edits += 1

            # if edits needed is > 1, no further checks needed. return False
            if edits > 1:
                return False

            # Checks to see if two strings can "lined up"
            #
            # If both string has the same length, increment both index.
            #   e.g
            #       "P L A C K"
            #       "B L A C K"
            #
            # Otherwise only increase the index of the longer string to see if
            # it "lines up" with the shorter string.
            #   e.g
            #       "B L A C K"
            #       "B L   C K"
            if len(longer) == len(shorter):
                i += 1
                j += 1
            else:
                i += 1

        # increase the loop index if no difference
        else:
            i += 1
            j += 1

    if edits > 1:
        return False

    return True


if __name__ == "__main__":
    a = "bale"
    b = "pale"
    print(one_away(a, b))
