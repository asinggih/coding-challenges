#!/usr/bin/env python3
#
# Code was written by asinggih (Aditya Singgih)

"""
Given an array of strings, remove each string that is an anagram of an
earlier string, then return the remaining array in sorted order

e.g.,

["code", "ecod", "framer", "doce", "frame"]
'doce' and 'ecod' are both anagrams of 'code' so they are removed.
'frame' and 'framer' are not anagrams due to the extra 'r' in 'framer'.

The final list of strings in alphabetical order is

['code', 'frame', 'framer']

Note: Problem set belongs to the owner (not me)

"""


def anagram(arr):

    for i in range(len(arr)):

        try:
            word = arr[i]
            lookup = set()  # charset for current word
            for char in word:
                lookup.add(char)

            # loop from the back so we can remove stuff
            for j in range(len(arr)-1, i, -1):

                # only check the compared word if length is the same as
                # current word
                if len(arr[i]) == len(arr[j]):
                    same = True  # initially we assume that theyre the same
                    for char in arr[j]:

                        # check if the compared word contains the same chars
                        # as current word
                        if char not in lookup:
                            same = False    # flip the flag
                            break

                    if same:
                        # remove it from the arr if it's an anagram of
                        # current word
                        arr.remove(arr[j])

        except:  # out of range exception, cos we removed some stuff(s) earlier
            print("here")
            return arr

    return arr


if __name__ == "__main__":

    # array = ["code", "aaagmnrs", "anagrams", "doce"]
    # array = ["aaa", "bbb", "ccc"]
    array = ["code", "ecod", "framer", "doce",   "frame"]

    output = anagram(array)

    output.sort(key=len)
    print(output)
