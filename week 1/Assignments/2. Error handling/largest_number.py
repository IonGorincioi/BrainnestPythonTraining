# Write a function that takes a list of integers as an argument,
# and returns the largest integer in the list. Use a try-except block
# to catch any ValueError exceptions that may be raised when attempting
# to compare elements that are not integers.


def convert_string_to_list(string):
    integers = []
    list_of_strings = string.split(",")
    for item in list_of_strings:
        item = int(item)
        integers.append(item)
    return integers


def largest_number(list_of_integers):
    largest = max(list_of_integers)
    return largest


try:
    user_input = input("Enter a list of integers separated by comma: ")
    numbers = convert_string_to_list(user_input)
    the_largest = largest_number(numbers)
    print(f"The largest number in the list is: {the_largest}")
except ValueError:
    print("Error! Please make sure you input only integers.")
