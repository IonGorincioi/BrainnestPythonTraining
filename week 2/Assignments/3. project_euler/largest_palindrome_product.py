# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of
# two 3-digit numbers.

def isPalindrome(string):
    char_list = []

    for character in string:
        char_list.append(character)

    rev_list = list(reversed(char_list))

    if char_list == rev_list:
        return True
    else:
        return False


def largest_palindrome_product(number_of_digits):
    ########################################################
    largest_product = 0
    # set the range of numbers that are going to be multiplied between
    # if the number has 2 digits, the range is 1 - 99
    start_digit_str = '1'  # the starting digit of a number will always be 1
    for i in range(1, number_of_digits):
        start_digit_str = start_digit_str + '0'

    # The range of n-digit numbers is start_value - end_value
    start_value = int(start_digit_str)
    end_value = int(start_digit_str + '0')

    print(f"The range of {number_of_digits}-digit numbers is: {start_value} - {end_value}")
    ########################################################

    # find the products of all the combination of numbers in this range
    for i in range(start_value, end_value):
        for j in range(start_value, end_value):
            product = i * j
            if isPalindrome(str(product)) and product > largest_product:
                largest_product = product
    # check if any of the results is palindrome

    return largest_product


print(largest_palindrome_product(4))
