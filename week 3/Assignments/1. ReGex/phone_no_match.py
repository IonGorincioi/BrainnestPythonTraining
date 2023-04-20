# Write a regular expression that matches a phone number in the format xxx-xxx-xxxx,
# where x is a digit. For example, the string "123-456-7890" should match.

import re

file_content = """ 
               The string "123-456-7890" should match.
               You also can try 879-356-9842 or 872-364-9807
               """

phone_no_pattern = r"\d{3}-\d{3}-\d{4}"

phone_numbers = re.findall(phone_no_pattern, file_content)

for phone_no in phone_numbers:
    print(phone_no)