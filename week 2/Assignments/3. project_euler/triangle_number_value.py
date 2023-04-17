# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?
from math import floor, sqrt


def triangle_number(level_number):
    """
    Takes a number as an input, calculates
    the triangle number having as many number
    of levels and returns the triangle number
    """
    triangle = (int(level_number ** 2 + level_number) // 2)
    return triangle


def number_of_divisors(number):
    """
    Counts the divisors of a number and
    returns the number of divisors
    """
    count = 0
    for potential_divisor in range(1, floor(sqrt(number)) + 1):
        if number % potential_divisor == 0:

            # check whether found divisors are equal (if equal, count only one)
            if potential_divisor ** 2 == number:
                count += 1
            else:
                count += 2
    return count


number = 0
while number_of_divisors(triangle_number(number)) <= 500:
    number += 1

print(triangle_number(number))
