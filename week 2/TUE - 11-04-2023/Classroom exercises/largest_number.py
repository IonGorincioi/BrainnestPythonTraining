# Create a for loop that iterates through a list of numbers
# and prints the largest number in the list.

numbers = [3, 5, 43, 7, 21, 87, 54, 13]

largest = 0
for number in numbers:
    if number > largest:
        largest = number

print(f"The largest number is: {largest}")