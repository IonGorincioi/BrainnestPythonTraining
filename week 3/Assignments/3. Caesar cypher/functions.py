def caesar_cypher(initial_text, key, cypher):
    """
    Gets a text as an input and returns the text encrypted/decrypted
    """
    final_text = ""
    alphabet = get_alphabet()

    # we shift only the characters inside the alphabet (letters)
    for character in initial_text:

        if character in alphabet:
            position = alphabet.index(character)

            if cypher == "e".lower():
                new_position = position + key
            elif cypher == "d".lower():
                new_position = position - key

            final_text += alphabet[new_position]
        else:
            # All the other characters will be added as they are
            # (spaces, commas, full stops, etc)
            final_text += character

    print(f"\n>>> {final_text}")


def get_alphabet():
    """ Opens and read the alphabet from a
        text file and returns the alphabet """
    with open("files/alphabet.txt", "r") as file:
        alphabet = []
        content = file.read()
        for character in content:
            if not character.isspace():
                alphabet.append(character)
        return alphabet
