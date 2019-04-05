#!/usr/bin/env python3
#
# Code was written by asinggih (Aditya Singgih)
#
#
# Note: Problemset belongs to the owner. Not me

"""

Given an array of numbers, find the largest difference within the array.

The difference can only be obtained by subtracting the current value.

with the value that has a lower index. 

If the values in the array are constantly decreasing, return -1

e.g.,

L = [10, 1, 4, 5, 3]

given that array, the function should return 4,
which was taken from 5-1


another case

L = [6, 5, 3, 1]

return -1, because there will be  no values with a lower index
that will be smaller than the current index

"""


def max_diff(arr):

    smallest = arr[0]
    largest_diff = -1

    for num in arr[1::]:

        if num-smallest > largest_diff:
            largest_diff = num-smallest

        if num < smallest:
            smallest = num

    return largest_diff


if __name__ == "__main__":

    # L = [7, 1, 2, 5]
    L = [6, 5, 4, 3, 2, 1]
    # L = [2, 3, 10, 2, 4, 8, 1]

    print(max_diff(L))
