# Write a function that takes a tuple as an argument and returns
# a new tuple with only the even elements from the original tuple.

def even_numbers(input_tuple):
    input_tuple = list(input_tuple)
    even = [item for item in input_tuple if item % 2 == 0]
    even = tuple(even)

    return even


numbers = (1, 2, 3, 4, 5)
print(f"Even elements: {even_numbers(numbers)}")
