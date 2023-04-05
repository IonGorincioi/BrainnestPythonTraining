def palindrome(string):
    char_list = []

    for character in string:
        char_list.append(character)

    rev_list = list(reversed(char_list))

    if char_list == rev_list:
        return f'"{user_input}" is palindrome'
    else:
        return f'"{user_input}" is not palindrome'


user_input = input("Enter a string: ")

result = palindrome(user_input)
print(result)
