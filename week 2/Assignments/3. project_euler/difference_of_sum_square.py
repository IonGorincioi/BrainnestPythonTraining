# The sum of the squares of the first ten natural
# numbers is, 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural
# numbers is, (1 + 2 + ... + 10)^2 = 3025
# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is, 3025 - 385 = 2640

# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.
import math


def sum_of_squares(range_number):
    total = 0
    for integer in range(1, range_number + 1):
        sq_integer = math.pow(integer, 2)
        total += sq_integer
    return total


def squared_sum(range_number):
    total = 0
    for integer in range(1, range_number + 1):
        total = total + integer
        squared_total = math.pow(total, 2)

    return squared_total


def difference_of_squares(the_range):
    sq_sum = squared_sum(the_range)
    sum_of_sq = sum_of_squares(the_range)
    difference = sq_sum - sum_of_sq
    return int(difference)


print(difference_of_squares(100))
