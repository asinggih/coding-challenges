#!/usr/bin/env python3
#
# Written by asinggih 10/01/19

'''
---------------------------------------
             Problem set
---------------------------------------
Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers
in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1],
the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

# -----------------------------------------------------------------

#                       First Solution

# -----------------------------------------------------------------


def sol_1(num_array):
    final_out = []
    total = 1
    # --------------------------------------------
    #   codeblock to handle zeroes in the array
    # --------------------------------------------
    zero_count = 0
    idx_of_zero = None
    for item in num_array:

        if item == 0:
            zero_count += 1
            # memorise the index of the zero
            idx_of_zero = num_array.index(item)
        else:
            total *= item

        # return all zeros if there's more than 1 zeros in the input array
        if zero_count > 1:
            return [0 for x in range(len(num_array))]

    # Final output will be all zeros except at the idx_of_zero
    # from the original array, which will be the product of all numbers
    # of the original array
    if zero_count:
        final_out = [0 for x in range(len(num_array))]
        final_out[idx_of_zero] = total

    # ------------------- end --------------------

    else:
        for item in num_array:
            final_out.append(total//item)

    return final_out


# -----------------------------------------------------------------

#               Second Solution (no division operator)

# -----------------------------------------------------------------

#   Algorithm summary (see example):
#
#   Basically what we do here is to doing the multipication from
#   both ends of the array, and let them complement each other
#
#   1. loop the array from left to right:
#       - build the multplication while carrying the previous num
#       - store each of the multiplication in a temp array x
#
#   2. do the same thing, but from the right to left (store in array y)
#
#   3. multiply each x[i] with y.reverse()[i] and store them
#      in the final array that will be returned

#   Example:
#   original input array = [3, 5, 2, 4]
#
#   x = [   1       3       3*5    3*5*2    ]
#   y = [   4*2*5   4*2     4      1        ] ------> this is in reversed form
#
#   out = [ x[0]*y[0] , x[1]*y[1] , x[2]*y[2] , x[3]*y[3]  ]


def sol_2(num_array):

    # Step 1
    array_a = []
    total_a = 1
    for item in num_array:
        array_a.append(total_a)
        total_a *= item

    # Step 2
    array_b = []
    total_b = 1
    for item in num_array[::-1]:
        array_b.append(total_b)
        total_b *= item

    # Step 3
    out = []
    for item in array_a:
        # need to use pop on array_b because we want to
        # start from the end of array_b array (see example)
        out.append(item*array_b.pop())
    return out


if __name__ == "__main__":
    x = [5, 4, 3, 2, 1]
    print("Solution 1")
    print(sol_1(x))
    print()
    print("Solution 2 - no div")
    print(sol_2(x))
