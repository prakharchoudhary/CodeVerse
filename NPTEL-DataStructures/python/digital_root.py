"""
Problem statement:

For any given positive integer, sum up all its digits until
we obtain a single digit number; then print its square root.
"""
import math


def sumNum(number):
    total = 0
    while number != 0:
        rem = number % 10
        total += rem
        number -= rem
        number /= 10
    return int(total)


def digital_root(number):
    while number > 9:
        number = sumNum(number)
    return number


output = """
Examples:
Digital root of 1233: %d;
Digital root of 1233: %d;
Digital root of 1233: %d;
Digital root of 1233: %d;
""" % (digital_root(1233), digital_root(65536),
       digital_root(9199999),
       digital_root(96999999))

print(output)
