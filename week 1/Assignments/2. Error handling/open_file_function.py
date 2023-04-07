# Write a function that takes a filename as an argument, and attempts to open the file.
# Use a try-except block to catch any FileNotFoundError exceptions that may be raised
# when attempting to open the file. If the file is successfully opened, the function
# should return the contents of the file.



def open_file(filepath):
    """
    open_file() function opens a file, reads its lines
    and returns the content as a list of string elements
    """
    filename = open(filepath, "r")
    file_content = filename.readlines()
    filename.close()
    return file_content


def filtering(file_content):
    """
    takes a string as an argument, splits it by the new line
    and returns the content as a list of string elements
    """
    filtered_content = []
    for item in file_content:
        item = item.split("\n")
        item = item[0]
        filtered_content.append(item)
    return filtered_content


try:
    file = open_file("files/file.txt")
    content = filtering(file)
    print(content)
except FileNotFoundError:
    print(f"ERROR! Make sure the file exists before opening it.")


