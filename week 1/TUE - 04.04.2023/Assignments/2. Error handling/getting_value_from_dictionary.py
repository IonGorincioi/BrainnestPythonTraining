# Write a function that takes a list of dictionaries as an argument,
# and returns the value of a specified key from each dictionary.
# Use a try-except block to catch any KeyError exceptions that may be
# raised when attempting to access a key that does not exist in a dictionary.

dictionaries = [{'one': 1, 'two': 2, 'three': 3},
                {'four': 4, 'five': 5},
                {'six': 6, 'seven': 7},
                {'eight': 8, 'nine': 9, 'ten': 10}]


def get_value(list_of_dict, key):
    for dictionary in list_of_dict:
        if key in dictionary:
            return f"{key} : {dictionary[key]}"

try:
    user_input = input("Enter the key: ")
    result = get_value(dictionaries, user_input)
    print(result)
except KeyError:
    print(f"{user_input} key is not present in dictionaries")
