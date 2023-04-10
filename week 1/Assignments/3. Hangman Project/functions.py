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
