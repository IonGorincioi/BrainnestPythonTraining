# Write a program that prompts the user for a string
# and checks whether the string is a palindrome
# (i.e., the string reads the same forward and backward).

user_input = input("Enter a string: ")
char_list = []

for character in user_input:
    char_list.append(character)

rev_list = list(reversed(char_list))

if char_list == rev_list:
    print(f'"{user_input}" is palindrome')
else:
    print(f'"{user_input}" is not palindrome')
