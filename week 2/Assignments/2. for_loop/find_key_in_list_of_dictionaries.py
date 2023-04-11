# Create a for loop that iterates through a list of dictionaries
# and prints the value of a specified key for each dictionary.

dictionaries = [{'country': 'France', 'capital': 'Paris', 'visits': 2},
                {'country': 'Germany', 'capital': 'Berlin', 'visits': 0},
                {'country': 'Ireland', 'capital': 'Dublin', 'visits': 7},
                {'country': 'Moldova', 'capital': 'Chisinau', 'visits': 13}]

user_input = input("Enter the key you'd like the value to be displayed: ")

try:
    for dictionary in dictionaries:
        for key in dictionary:
            key = user_input
        print(dictionary[key])
except KeyError:
    print(f"The key '{user_input}' doesn't exist in dictionary.")