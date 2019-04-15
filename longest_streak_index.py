#!/usr/bin/env python3
#
# Code was written by asinggih (Aditya Singgih))
#
# Note: Problem set belongs to the owner (not me)

"""

From a given array, find the longest streak, 
and return the index of the first number in that longest streak.

If there's no increasing sequence, return -1

"""


def start_index(arr):

    lookup = dict()

    longest_streak = 0
    for i in range(len(arr)-1):
        if arr[i+1] > arr[i]:
            longest_streak += 1
        elif arr[i+1] <= arr[i]:
            lookup[i] = longest_streak
            longest_streak = 0
    lookup[len(arr)-1] = longest_streak

    start_idx = None
    largest = 0
    for idx in lookup:
        if lookup[idx] >= largest:
            start_idx = idx
            largest = lookup[idx]

    if largest == 0:
        return -1

    return start_idx - largest


if __name__ == "__main__":

    # L = [5, 6, 7, 1, 2, -1, 10, 12, 13, 14]
    # L = [10, 9, 8, 7, 5, 1]
    # L = [5, 6, 7, -1, 2, 3, 0, 13, 14]
    L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]

    print(start_index(L))
