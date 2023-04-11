# Create a for loop that iterates through a list of
# numbers and prints the largest number in the list.

largest = 0
numbers = [2, 43, 76, 23, 98, 9]
for number in numbers:
    if number > largest:
        largest = number

print(f"The largest number is: {largest}")