# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of
# two 3-digit numbers.


def isPalindrome(string):
    """
    Takes a string and checks whether it is a palindrome
    """
    char_list = []
    for character in string:
        char_list.append(character)
    rev_list = list(reversed(char_list))
    if char_list == rev_list:
        return True
    else:
        return False


def n_digit_range(number_of_digits):
    """
    Takes a number "n" and defines the range of all n-digit number.
    Then adds all numbers within the range in a list and returns the list
    """
    start_digit_str = '1'  # the starting digit of a number will always be 1
    for i in range(1, number_of_digits):
        start_digit_str = start_digit_str + '0'

    # The range of n-digit numbers is start_value - end_value
    start_value = int(start_digit_str)
    end_value = int(start_digit_str + '0')

    # print(f"The range of {number_of_digits}-digit numbers is: {start_value} - {end_value}")
    the_range = range(start_value, end_value)
    return list(the_range)


def all_products(range_list):
    """
    Takes a list as an input and calculates all possible products among numbers in the list,
    adds all the products in a new list and returns the products list
    """
    products_list = []
    for i in range_list:
        for j in range_list:
            product = i * j
            products_list.append(product)
    return products_list


def largest_palindrome_product(products_list):
    """
    Check which product from the list is palindrome,
    determines the largest one and returns it
    """
    largest_product = 0
    for product in products_list:
        if isPalindrome(str(product)) and product > largest_product:
            largest_product = product

    return largest_product


user_input = int(input("Enter the number of digits: "))
number_range = n_digit_range(user_input)
# print(number_range)

products = all_products(number_range)
print(products)

largest_palindrome = largest_palindrome_product(products)
print(f"The largest palindrome product of two {user_input}-digit numbers is: {largest_palindrome}")

