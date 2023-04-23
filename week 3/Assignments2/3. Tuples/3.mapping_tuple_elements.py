# Write a function to find the frequency of elements in a tuple,
# and return a dictionary mapping each element to its frequency.

def find_most_common_element(input_tuple):
    frequency = {}
    result = {}
    for element in input_tuple:

        # check whether the element in the tuple is a number
        if not str(element).isnumeric():
            element = element.capitalize()

        # counts the frequency of each element
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1

        # assigns "element : frequency" key-value pairs in dictionary
        result[element] = frequency[element]

    return result


names = ("John", "Mary", "Ion", "maRy", "Michael", "iON")
numbers = (11, 23, 4, 23, 5, 6, 23, 34, 33, 12, 23, 14)

print(find_most_common_element(names))
print(find_most_common_element(numbers))