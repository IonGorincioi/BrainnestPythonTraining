import random


def words(filepath):
    """
    This function opens a file, copy its content in a list,
    splits the elements by the new line and gets rid of the
    new lines and copies the elements in another list
    """
    new_content = []
    with open(filepath, 'r') as file:
        content = file.readlines()
    file.close()
    for item in content:
        item = item.split("\n")
        new_content.append(item[0])
    return new_content


def random_word(word_list):
    """
    This function selects and returns a random word from the list
    """
    selected_word = random.choice(word_list)
    return selected_word


def hide_word(selected_word):
    """
    This function hides the letters of the selected
    word, returning a number of underscores.
    """
    random_word(selected_word)
    for letter in selected_word:
        hidden_word = ['_'] * len(selected_word)
    return hidden_word


def display_word(hidden_word):
    """
    Displays underscores instead of letters  on the screen
    """
    return f"\nWord: {' '.join(hidden_word)}"


def check_letter_existence(selected_word, letter_guessed):
    """
    Checks whether the guessed letter is present in randomly selected word
    """
    letter_exists = False
    for index in range(len(selected_word)):
        letter = selected_word[index]
        if letter == letter_guessed:
            letter_exists = True
    return letter_exists

    #
    #         display[index] = letter_guessed
    #
    # print(display_word(selected_word[index]))


def unmask_guessed_letters(selected_word, ):
    letter_guessed = check_letter_existence(selected_word, )
    display = hide_word(selected_word)
    if letter_guessed:
        for index in range(len(selected_word)):
            display[index] = letter_guessed
        print(display_word(selected_word))

# def display_incomplete_word(selected_word, guess):
#     hidden_word = hide_word(selected_word)
#     for index in range(len(selected_word)):
#         letter = hidden_word[index]
#         if letter == guess:
#             hidden_word[index] = letter
#     return display_word(selected_word)

#     if letter == user_guess:
#         display[index] = letter
# print(f"\nWord: {' '.join(display)}")


available_words = words("files/words.txt")
print(available_words)

word_to_guess = random_word(available_words)
print(word_to_guess)

masked_word = hide_word(word_to_guess)
print(masked_word)

print(display_word(masked_word))

end_of_game = False
while not end_of_game:
    user_guess = input("Guess a letter: ").lower()

    print(check_letter_existence(word_to_guess, user_guess))
    # unmask_guessed_letters(word_to_guess)


#     incomplete_word = display_incomplete_word(word, user_guess)
#     print(incomplete_word)
