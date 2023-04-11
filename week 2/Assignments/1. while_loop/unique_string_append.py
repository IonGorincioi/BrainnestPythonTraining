# Create a while loop that repeatedly takes user input and
# appends it to a list, but only if the input is a unique string.

tasks = []
status = ""
loop_end = False
print("If you don't want to enter any other tasks type 'done'. ")
while not loop_end:
    user_input = input("Add your task: ")
    if user_input.lower() != 'done':
        user_input = user_input.strip()
        if user_input not in tasks:
            tasks.append(user_input)
        else:
            print(f"'{user_input}' is already in the list.")
        print(tasks)
    else:
        loop_end = True

print(f"The tasks are: {tasks}")

