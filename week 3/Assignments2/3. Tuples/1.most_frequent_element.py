# Write a function to find the most common elements in a tuple.


def find_most_common_element(tuple_of_elements):
    counter = 0
    for element in tuple_of_elements:
        current_element = tuple_of_elements.count(element)
        if current_element > counter:
            counter = current_element
            most_frequent = element
    return most_frequent


numbers = (1, 2, 4, 3, 5, 6, 3, 4, 3, 2, 3, 4)
names = ("John", "Mary", "Ion", "Mary", "Michael")


print(find_most_common_element(numbers))
print(find_most_common_element(names))
