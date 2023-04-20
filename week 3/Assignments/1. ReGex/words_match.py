# Write a regular expression that matches a string that starts with a word,
# followed by one or more whitespace characters, followed by another word.
# For example, the string "hello world" should match.

import re

file_content = """ 
               *** Hello world! ***
               """

pattern = r"\w+\W\w+"

the_substring = re.findall(pattern, file_content)

print(the_substring)