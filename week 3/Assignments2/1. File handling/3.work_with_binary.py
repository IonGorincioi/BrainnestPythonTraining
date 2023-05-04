# Write a Python program that reads a binary file and converts it into a hexadecimal
# string. The program should output the hexadecimal string to a text file.

with open("files/binary.txt", "rb") as file:
    binary_content = file.read()
    while binary_content != '':
        text = ascii(binary_content)
        # print(text)
        binary_content = file.read(8)
    print(binary_content)