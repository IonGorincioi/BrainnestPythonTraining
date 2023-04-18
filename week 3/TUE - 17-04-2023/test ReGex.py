# from re import compile
import re

text = "I am 37 years old. I was born on 13-08-1984."
text1 = "2023"


pattern = r'\d+'
# number = re.search(pattern, text)
# number = re.match(pattern, text)
number = re.fullmatch(pattern, text1)
print(number)

print('Matched string:', number.group())
print('Starting index:', number.start())
print('End position:', number.end())
print('Position:', number.span())




