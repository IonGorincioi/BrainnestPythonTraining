# Write a Python program that reads a text file and prints
# the number of lines, words, and characters in the file.

file = open("files/file.txt", "r")
content = file.readlines()
file.close()

number_of_lines = 0
number_of_words = 0
number_of_characters = 0

for line in content:
    words = line.split()
    number_of_lines += 1
    number_of_words += len(words)
    number_of_characters += len(line)


print(f""" 
      The file contains:
      {number_of_lines} lines
      {number_of_words} words
      {number_of_characters} characters
      """)