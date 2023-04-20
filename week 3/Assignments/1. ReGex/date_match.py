# Write a regular expression that matches a date in the format dd/mm/yyyy.
# For example, the string "01/01/2021" should match.

import re

file = """For example, the string 01/01/2021 should match. 
          Today, 20/04/2023, I have learnt about ReGex. 
       """

date_pattern = re.findall(r"\d{1,2}/\d{1,2}/\d{4}", file)
for date in date_pattern:
    print(date)
