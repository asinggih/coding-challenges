#!/usr/bin/env python3
#
# Code was written by asinggih (Aditya Singgih)
#
# Note: Problemset belongs to the owner. Not me

"""
Write a function:

function solution(A);
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Assume that:

N is an integer within the range [1..100,000]
Each element of array A is an integer within the range [−1,000,000..1,000,000]
"""


def solution(A):
    seen = set()
    for item in A:
        if item > 0:
            seen.add(item)

    if not seen:
        return 1

    for number in range(1, len(A)+2):
        if number not in seen:
            return number


if __name__ == "__main__":

    A = [1, 3, 6, 4, 1, 2]
    B = [1, 2, 3, 4, 5]
    C = [-1, -3]

    print(solution(B))
