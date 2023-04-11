# Create a while loop that repeatedly takes user input and appends
# it to a list, but only if the input is a number greater than 10.

numbers = []
end_of_loop = False
status = ""
print("Type 'done' to exit. ")
while not end_of_loop:
    user_input = input("Enter an input: ")

    if user_input.lower() != 'done':
        user_input = user_input.strip()

        if user_input.isnumeric():
            user_input = int(user_input)
            if user_input > 10:
                numbers.append(user_input)
    else:
        end_of_loop = True

    print(numbers)

