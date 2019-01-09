#!/usr/bin/env python3
#
# Written by asinggih 09/01/19

'''
---------------------------------------
             Problem set
---------------------------------------
Given a list of numbers and a number k, return whether any two numbers from
the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''


def find_sum(k, num_array):
    seen = set()                    # keep track of numbers that have been seen
    for i in num_array:
        complement = k-i            # the number needed to get to k
        if complement in seen:
            return True
        seen.add(i)
    return False


if __name__ == "__main__":
    nums = [10, 15, 3, 7]
    k = 17
    print(find_sum(k, nums))
