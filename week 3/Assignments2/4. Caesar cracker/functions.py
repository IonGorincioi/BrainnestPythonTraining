
def get_alphabet():
    """ Opens and read the alphabet from a
        text file and returns the alphabet """
    with open("alphabet.txt", "r") as file:
        alphabet = []
        content = file.read()
        for character in content:
            if not character.isspace():
                alphabet.append(character)
        return alphabet




def decrypted_message(message, alphabet, key):
    new_message = ""
    for ch in message:
        if ch in alphabet:
            position = alphabet.index(ch)
            new_position = position - key
            new_message += alphabet[new_position]
        else:
            new_message += ch

    return new_message
