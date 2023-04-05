# Write a program that prompts the user for a number and checks whether
# the number is a prime number (i.e., only divisible by 1 and itself).

user_input = int(input("Enter an integer number: "))

if user_input == 1:
    print(f"{user_input} is not a prime number")

elif user_input > 1:
    for i in range(2, user_input):
        if user_input % i == 0:
            print(f"{user_input} is not a prime number.")
            break
        else:
            print(f"{user_input} is prime number")
            break