import math


def number_to_exp(base, exp):
    """
    Raises a number to a power and
    returns the result
    """
    result = int(math.pow(base, exp))
    return result


def sum_of_digits(integer):
    """
    Takes a number as an input and calculates
    the sum of all the number's digits
    """
    digits_sum = 0
    for digit in str(integer):
        digits_sum += int(digit)
    return digits_sum


number = number_to_exp(2, 1000)
total = sum_of_digits(number)
print(f"The sum of digits is: {total}")

