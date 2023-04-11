# Create a for loop that iterates through a list
# of numbers and prints the square of each number.

numbers = [2, 3, 6, 8, 12, 10, 9, 7]

square = [number ** 2 for number in numbers]
print(f"List of squares: {square}")