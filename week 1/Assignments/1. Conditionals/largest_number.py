# Write a program that takes in a list of integers and returns
# the largest number in the list that is also divisible by 3.

user_input = input("Enter a list of numbers: ")
user_strings = user_input.split(",")
numbers = []

for item in user_strings:
    item = int(item)
    if item % 3 == 0:
        numbers.append(item)

largest = max(numbers)

print(f"The largest number divisible by 3 is: {largest}")
