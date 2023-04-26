# Given a list of words, write a function to return a set of all anagrams in the list.


def anagrams(list_of_words):
    result = {}
    for word in list_of_words:

        # sort the letters of each word in the list
        sorted_word = str(sorted(word))

        # check is any words match and add them in a list
        if sorted_word in result:
            result[sorted_word].append(word)
        else:
            result[sorted_word] = [word]

    return list(result.values())


words = ["dog", "python", "car", "god", "arc", "field", "typhon", "flied"]
print(anagrams(words))
