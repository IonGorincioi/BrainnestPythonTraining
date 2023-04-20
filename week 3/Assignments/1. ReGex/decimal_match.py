# Write a regular expression that matches a string that contains a number
# with exactly two decimal places. For example, the string "1.23" should match,
# but the string "1.234" should not match.

import re

file_content = "12.345, 2.86, 45.3, 6.76"

pattern = r"\d+.\d{2}\b"

two_decimal_place = re.findall(pattern, file_content)

for dec in two_decimal_place:
    print(dec)
