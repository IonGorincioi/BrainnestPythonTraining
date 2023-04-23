# Write a Python program that reads a text file containing numbers
# and calculates the sum of all the numbers in the file.

with open("files/numbers.txt", "r") as file:
    numbers = file.readlines()

    number_list = []
    total = 0
    for number in numbers:
        number = number.split(",\n")
        total += int(number[0])
        number_list.append(int(number[0]))

    print(number_list)
    print(f"Sum: {total}")
