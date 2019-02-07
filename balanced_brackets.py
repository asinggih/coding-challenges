#!/usr/bin/env python3
#
# Written by asinggih 07/02/19

"""
---------------------------------------
             Problem set
---------------------------------------
Given a string of round, curly, and square open and closing brackets,

return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def balanced_brackets(list_of_brackets):
    """
    A function to check if the given list of brackets are well formed
    """

    if list_of_brackets.strip() == "":  # check for empty strings
        return False

    stack = []
    bracket_pair = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    for bracket in list_of_brackets:
        if bracket in bracket_pair:
            stack.append(bracket)
        else:  # if bracket is a closing bracket
            try:
                popped = stack.pop()
                if bracket != bracket_pair[popped]:
                    return False
            except:
                return False

    if stack:  # if there's still item in the stack
        return False

    return True


if __name__ == "__main__":

    a = "([])[]({})"
    b = "([)]"
    c = "((()"
    d = ""
    e = "[{(())}]{({})}"

    print(balanced_brackets(a))
    print(balanced_brackets(b))
    print(balanced_brackets(c))
    print(balanced_brackets(d))
    print(balanced_brackets(e))
