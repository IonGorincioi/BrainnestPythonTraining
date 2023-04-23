# Write a function to find all unique elements in a tuple and return them in a new tuple.

def find_unique_elements(input_tuple):
    elements = []
    element_list = list(input_tuple)

    # checks whether elements are not numbers and makes them case un-sensitive
    for element in element_list:
        if not str(element).isnumeric():
            element = element.capitalize()

        # add only new elements in the list
        if element not in elements:
            elements.append(element)

    unique_elements = tuple(elements)
    return unique_elements


numbers = (3, 2, 4, 5, 4, 3, 5, "Ion", 4, 3, 2, "ioN", 8)
names = ("John", "Mary", "Ion", "Mary", "MicHael", "ION")

print(f"{find_unique_elements(numbers)}")
print(f"{find_unique_elements(names)}")
