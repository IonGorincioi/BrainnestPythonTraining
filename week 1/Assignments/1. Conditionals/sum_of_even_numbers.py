# Write a program that takes in a list of integers
# and returns the sum of all even numbers in the list.

user_input = input("Enter a list of numbers separated by comma: ")
list_of_strings = user_input.split(",")
numbers = []
for item in list_of_strings:
    item = int(item)
    if item % 2 ==0:
        numbers.append(item)

total = sum(numbers)

print(f"The sum of even numbers is: {total}")