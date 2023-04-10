"""
The hangman game is a word guessing game where the player is
given a word and has to guess the letters that make up the word.
The player is given a certain number of tries
(no more than 6 wrong guesses are allowed)
to guess the correct letters before the game is over.
"""
import random

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''
import random

display = []  # a list that will hold the letters of a word to be guessed
guessed_letters = []  # a list that will hold all the letters used by the user
wrong_guesses = 6

# Open a text file that contains a list of words
# and copies all the words in a list
with open("Assignments/3. Hangman Project/files/words.txt", 'r') as file:
    content = file.readlines()
file.close()

# iterate over the words from the list, splitting them by
# new line and copies all the elements in a new list
new_content = []
for item in content:
    item = item.split("\n")
    new_content.append(item[0])
content = new_content

# randomly choose a word from the "content" list
word = random.choice(content)

# iterates over letters in the word and replace each letter
# with an underscore in "display" list
for letter in word:
    display = ['_'] * len(word)

# displays a series of underscores on the screen
print(f"\nWord: {' '.join(display)}")

end_of_game = False
while not end_of_game:

    """prompt the user to enter a letter"""
    user_guess = input("Guess a letter: ").lower()

    """the letter is added to "guessed_letters" list """
    # guessed_letters.append(user_guess)

    """Check if the letter is already in "guessed_letters" list and return a message"""
    # Checks if user guessed the letter already
    if user_guess in guessed_letters:
        print(f"You already guessed letter {user_guess} ")

    """Check whether the user guessed any letters and displays them"""
    # iterate over the letters in the word and displays
    # the right letters inside "display" list.
    for index in range(len(word)):
        letter = word[index]
        if letter == user_guess:
            display[index] = letter
    print(f"\nWord: {' '.join(display)}")

    """Throw a message if user uses the same letter multiple times, """
    # check for the wrong guesses
    if user_guess in guessed_letters:
        print(f"You already tried {user_guess}")

    """If user_guess does not match any letter in the word, it trows a message and 
        decrement the amount of wrong guesses allowed"""
    if user_guess not in word:
        print(f"The word doesn't contain letter {user_guess}")
        wrong_guesses = wrong_guesses - 1
        # print(f"You have {wrong_guesses} guesses left.")
        if wrong_guesses == 0:
            end_of_game = True
            print(f'You lose.')
            break

        guessed_letters.append(user_guess)
        print(f"Used letters: {guessed_letters}")
        print(f"\nWord: {' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print("You win")
    print(f"You have {wrong_guesses} guesses left.")
print(f"You guessed the word {word}")
