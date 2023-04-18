# Write a list comprehension that takes a list of strings
# and returns a new list with only the strings that
# contain at least one vowel, in reverse order.

vowels = ['a', 'e', 'i', 'o', 'u']
string = "hello python, tks"
new_string = ""
words = string.split(" ")
for word in words:
    for ch in word:
        if ch in vowels:
            new_string += word + " "
print(new_string)