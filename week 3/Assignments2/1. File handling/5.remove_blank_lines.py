# Write a Python program that reads a text file and removes all the blank lines.
# The modified text should be written back to the file.


with open("files/file_with_blanks.txt", "r") as file:
    content = file.readlines()

with open("files/file_with_blanks.txt", 'w') as file:
    for line in content:
        if not line.isspace():
            file.write(line)
