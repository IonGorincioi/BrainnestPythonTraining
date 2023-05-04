# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

file = open("numbers.txt", 'r')
content = file.readlines()
file.close


total = 0
for line in content:
    number = line.split("\n")
    number = int(number[0])
    total += number


result = str(total)[0: 10]
print(result)