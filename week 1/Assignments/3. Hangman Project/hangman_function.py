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


display = []  # a list that will hold the letters of a word to be guessed
used_letters = []  # a list that will hold all the letters used by the user
wrong_guesses = 6

print("-----------------------------------------------")
print(f"You are allowed {wrong_guesses} wrong guesses.")


available_words = words("files/words.txt")
word_to_guess = random_word(available_words)

for letter in word_to_guess:
    hidden_word = ['_'] * len(word_to_guess)

print(f"\n\t\tWord: {' '.join(hidden_word)}\n")
print("-----------------------------------------------")
end_of_game = False
while not end_of_game:

    print(f"You have {wrong_guesses} tries left")
    user_guess = input("Guess a letter: ").lower()

    # Check if user guessed the letter already
    if user_guess in used_letters:
        print(f"You have already guessed letter {user_guess} ")
    #
    elif user_guess not in used_letters:
        used_letters.append(user_guess)

        # iterate over the letters in the word and displays
        # the right letters inside "display" list.
        for index in range(len(word_to_guess)):
            letter = word_to_guess[index]
            if letter == user_guess:
                hidden_word[index] = letter

        if user_guess not in hidden_word:
            print(f"The word doesn't contain letter {user_guess}")
            wrong_guesses = wrong_guesses - 1
            if wrong_guesses == 0:
                end_of_game = True
                print(f'\nYou lose!')
                break

    print(f"Used letters: {used_letters}\n")
    print(f"\t\tWord: {' '.join(hidden_word)}\n")
    if '_' not in hidden_word:
        end_of_game = True
        print("Congratulation! You win!")

    print("-----------------------------------------------")
print(f'The word is: "{word_to_guess}".')
