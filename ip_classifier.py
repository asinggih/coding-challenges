#!/usr/bin/env python3

import re

"""

https://www.hackerrank.com/challenges/ip-address-validation/problem


Determine whether input is IPv4, IPv6, or Neither

IPv4 was the first publicly used Internet Protocol which used 4 byte addresses
which permitted for 232 addresses. The typical format of an IPv4 address is
A.B.C.D where A, B, C and D are Integers lying between
0 and 255 (both inclusive).

IPv6, with 128 bits was developed to permit the expansion of the address space.
To quote from the linked article: The 128 bits of an IPv6 address are
represented in 8 groups of 16 bits each. Each group is written as
4 hexadecimal digits and the groups are separated by colons (:).

The address 2001:0db8:0000:0000:0000:ff00:0042:8329 is an
example of this representation.

Consecutive sections of zeros will be left as they are.
An IPv6 value such as "...:0:..." or "...:5:..." is address-wise identical
to "...:0000:..." or "...:0005:....". Leading zeros may be omitted in
writing the address.

Sample input:
3
This line has junk text.
121.18.19.20
2001:0db8:0000:0000:0000:ff00:0042:8329

Sample output:
Neither
IPv4
IPv6

"""


def classify_ip(ip):
    # This is a proper regex to grep IPv4 Address
    # ^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$
    ipv4_patt = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    ipv4 = ipv4_patt.match(ip)

    ipv6_patt = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')
    ipv6 = ipv6_patt.match(ip)

    if ipv4:
        temp = ipv4.group().split(".")
        for item in temp:
            x = int(item)
            if x > 255:
                return "Neither"

        return "IPv4"

    elif ipv6:
        return "IPv6"

    else:
        return "Neither"


if __name__ == "__main__":

    input_count = int(input())

    out = []

    for i in range(input_count):
        ip = input()
        out.append(classify_ip(ip))

    for i in out:
        print(i)
