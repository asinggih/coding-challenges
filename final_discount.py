#!/usr/bin/env python3

"""

Given an array of prices, for each prices, determine if it will be
discounted or not.

discount is determined by the closest lower price on its right.

e.g.,

L = [4,1,6,2]
L[0] will have a final price of 4-1
L[1] will have a final price of 1-0 (no discount) since nothing is
        lower than L[1] on its right
....
L[3] will have a final price of 2-0

output should be in 2 lines
- total final price after discount
- index of non discounted item separated by space .e.g,
    1 3

constraints:
    n is prices array size
    1 <= n <= 10**5

    1 <= price <= 10**5


"""


def final_discount(prices):

    stack = []
    result = []

    for i in range(len(prices)-1, -1, -1):
        while stack != [] and stack[len(stack)-1] > prices[i]:
            stack.pop()
        if stack != []:
            result.append(stack[len(stack)-1])

        stack.append(prices[i])

    print(sum(result))


# def final_discount(prices):

#     no_discount = []
#     final_price = 0
#     for i in range(len(prices)):

#         for j in range(i+1, len(prices)):
#             if prices[j] <= prices[i]:
#                 final_price += prices[i] - prices[j]
#                 break

#             if j == len(prices)-1:
#                 final_price += prices[i]
#                 no_discount.append(str(i))
#                 break

#     final_price += prices[len(prices)-1]
#     no_discount.append(str(len(prices)-1))

#     print(final_price)
#     print(" ".join(no_discount))


if __name__ == "__main__":

    # prices = [5, 1, 3, 4, 6, 2]
    prices = [5, 4, 5, 1, 3, 3, 8, 2]

    final_discount(prices)
