# Write a program that prompts the user for their age and checks
# whether they are old enough to vote (i.e., 18 years old or older).

age = int(input("Enter Your age: "))

if age < 18:
    print("You are too young. You are not eligible to vote.")
else:
    print("You are eligible to vote")