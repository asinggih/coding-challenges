#!/usr/bin/env python3
#
# Written by asinggih 07/02/2019

"""
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as
a single count and character. For example, the string "AAAABBBCCDAA"
would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string
to be encoded have no digits and consists solely of alphabetic
characters. You can assume the string to be decoded is valid.
"""


def rlencode(raw_string):
    """
    Encoding raw string into run-length
    """

    out_container = []
    memorised_char = None
    count = 1
    for char in raw_string:

        if memorised_char is None:
            memorised_char = char   # initial value for the memorised char

        elif char == memorised_char:
            count += 1

        else:
            # out_string += str(count) + memorised_char
            out_container.append(str(count))
            out_container.append(memorised_char)
            memorised_char = char   # update the memorised char
            count = 1               # reset count after looking at a new char

    # adding the last group of char(s) into out_string
    out_container.append(str(count))
    out_container.append(memorised_char)

    # join the list to create a desired output format
    out_string = "".join(out_container)

    if len(out_string) < len(raw_string):
        return out_string
    else:
        return raw_string


def rldecode(encoded_string):
    """
    Decoding the run-length encoded string
    """

    decoded = ""
    count = 0
    for i in range(len(encoded_string)):
        if i % 2 == 0:          # Even index. Means we're looking at the count
            try:
                count = int(encoded_string[i])
            except ValueError:  # input is already decoded
                return encoded_string

        else:    # Odd index. Looking at the char
            decoded += encoded_string[i] * count

    return decoded


if __name__ == "__main__":
    a = "AAAABBBCCDAA"
    b = "AAAB"
    c = "4A3B2C1D2A"
    d = "AABBCCAA"
    e = "aabcccccaaa"

    print(rldecode(rlencode(a)) == a)
    # print(rlencode(a))
