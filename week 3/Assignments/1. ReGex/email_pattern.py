# Write a regular expression that matches a valid email address.
# For example, the string "example@example.com" should match.

import re

file_content = """ 
               The string "example@example.com" should match
               thisemailaddress@gmail.com should match as well
               """

email_pattern = r"\w+@\w+.\w{3}"
emails = re.findall(email_pattern, file_content)

for email in emails:
    print(email)