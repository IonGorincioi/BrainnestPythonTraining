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

# def open_file(filepath):
with open("files/words.txt", 'r') as file:
    content = file.readlines()
file.close()

# def split_items(content)
new_content = []
for item in content:
    item = item.split("\n")
    new_content.append(item[0])
content = new_content

# def hide_word(content)
display = []  # optional
word = random.choice(content)
for letter in word:
    display = ['_'] * len(word)

# def print_word():
print(f"\nWord: {display}")

end_of_game = False
while not end_of_game:
    user_guess = input("Guess a letter: ").lower()

    # def used_letter():
    """ 
    Checks if user attempted to guess the letter already
    """
    if user_guess in display:
        print(f"You already guessed letter {user_guess} ")

    # def display_letter():
    for index in range(len(word)):
        letter = word[index]
        if letter == user_guess:
            display[index] = letter
    print(f"\nWord: {' '.join(display)}")

guessed_letters = []
wrong_guesses = 1
if user_guess in guessed_letters:
    print(f"You already tried {user_guess}")

elif user_guess not in word:
    print(f"The word doesn't contain letter {user_guess}")
    wrong_guesses -= 1
    if wrong_guesses == 0:
        end_of_game = True
        print(f'You lose.')

    guessed_letters.append(user_guess)
    print(f"attempts: {guessed_letters}")
    print(f"\nWord: {' '.join(display)}")

    if not _ in ' '.join(display):
        end_of_game = True
        print("You win")
print(f"You guessed the word {word}")
