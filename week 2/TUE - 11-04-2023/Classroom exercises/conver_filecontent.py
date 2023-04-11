try:
    file = open("file.txt", "r")
    content = file.readline()
    file.close()

    words = content.split(" ")
    for word in words:
        print(word.upper())
except FileNotFoundError:
    print("This file does not exist")