# Create a while loop that generates random numbers and adds them to
# a list until the sum of all numbers in the list is greater than 100.

import random

numbers = []
total = 0
end_of_numbers = False

while not end_of_numbers:
    number = random.randint(1, 20)
    total = total + number
    numbers.append(number)
    if total > 100:
        end_of_numbers = True

print(f"Random numbers: {numbers}\nSum: {total}")