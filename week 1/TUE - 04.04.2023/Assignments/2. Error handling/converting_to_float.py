# Write a function that takes a list of strings as an argument, and
# returns a new list containing only the strings that can be successfully
# converted to a float. Use a try-except block to catch any ValueError
# exceptions that may be raised when attempting to convert a string to a float.


def convert_to_float(string):
    list_of_strings = string.split(",")
    new_list = []
    for element in list_of_strings:
        if element.strip().isnumeric():
            element = float(element)
            new_list.append(element)
        else:
            continue
    return new_list


try:
    user_input = input("Enter a number of elements separated by comma (no spaces): ")
    result = convert_to_float(user_input)
    print(result)
except ValueError:
    print("ERROR!")
