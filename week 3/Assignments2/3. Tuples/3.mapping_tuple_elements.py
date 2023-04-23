# Write a function to find the frequency of elements in a tuple,
# and return a dictionary mapping each element to its frequency.

def find_most_common_element(input_tuple):
    frequency = {}
    for element in input_tuple:
        element = element.capitalize()
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1

    for key, value in frequency.items():
        print(key, ':', value)


names = ("John", "Mary", "Ion", "Mary", "Michael", "iON")
print(find_most_common_element(names))
