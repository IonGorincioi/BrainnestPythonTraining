# Create a while loop that repeatedly takes user input
# and adds the input to a list until the user enters "done".

status = ""
tasks = []
end_of_loop = False
print("If you don't want to enter any tasks type 'done'. ")
while not end_of_loop:
    user_input = input("Enter a task: ")

    if user_input.lower() == 'done':
        end_of_loop = True

    elif status != 'done':
        tasks.append(user_input)

    print("Your tasks: ", tasks)
