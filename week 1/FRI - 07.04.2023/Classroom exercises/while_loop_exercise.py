#                           1.first_10_digits_sum:
# Write a program which repeatedly reads numbers until the
# user enters `done`. Once `done` is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.

# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

# from statistics import mean
# functions to be used: sum(), len(), mean()

while True:
    count = 0
    total = 0
    user_input = input("Enter a number: ")
    if user_input != 'done':
        total += int(user_input)
        count += 1
        average = total/count
    else:
        print("----------------------")
        print(f"The sum of numbers: {total}.\nYou entered {count} numbers.\nThe average is {average}")


