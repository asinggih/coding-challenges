#!/usr/bin/env python2.7
#
# Code was written by asinggih (Aditya Singgih)
#
#
# Note: Problemset belongs to the owner. Not me

"""

Given a spaced-separated string of numbers,

return the number that occurs the most.

If 2 or more numbers have the same occurences, return the largest number.

If all numbers have same occurences, return the largest number

"""


def find_most_freq(string):

    array = userinput.split(" ")
    array = [int(i) for i in array]

    distinct = set(array)
    lookup = dict()

    largest_num = array[0]
    for i in array:
        if i > largest_num:
            largest_num = i

        if i in lookup:
            lookup[i] += 1
        else:
            lookup[i] = 1

    output = None
    largest_count = 0
    for num in distinct:
        if lookup[num] >= largest_count:
            largest_count = lookup[num]
            output = num

    if output is None:
        return largest_num

    return output


if __name__ == "__main__":

    # userinput = "1 5 1 4 9 0 4"
    # userinput = "1 5 1 9 0 4"
    userinput = "1 5 10 4 9 0"

    print(find_most_freq(userinput))
