# Write a function that takes a list of integers as an argument, and returns
# the sum of the integers. Use a try-except block to catch any ValueError
# exceptions that may be raised when attempting to convert a string to an integer.


def convert_to_int(user_string):
    integers = []
    user_list = user_string.split(",")
    for item in user_list:
        item = int(item)
        integers.append(item)
    return integers


def sum_of_int(list_of_ints):
    total = 0
    for item in list_of_ints:
        total = total + item
    return total


try:
    user_input = input("Enter a list of integers separated by comma: ")
    list_of_int = convert_to_int(user_input)
    result = sum_of_int(list_of_int)
    print(f"Sum: {result}")
except ValueError:
    print("ERROR! You must input only numbers separated by comma. Please try again")
