# Create a while loop that repeatedly takes user input and keeps
# track of the highest number entered until the user enters "done".

print("Type 'done' to exit. ")
largest = 0
numbers = []
status = ""
end_of_loop = False

while not end_of_loop:
    user_input = input("Enter a number: ")

    if user_input.lower() != 'done':
        user_input = user_input.strip()
        if user_input.isnumeric():
            user_input = int(user_input)
            numbers.append(user_input)
            for number in numbers:
                if number > largest:
                    largest = number

            print(f"The largest number entered is : {largest}")
        else:
            print("Please enter only numbers.")
    else:
        end_of_loop = True


print(f"The largest number in the list is : {largest}")