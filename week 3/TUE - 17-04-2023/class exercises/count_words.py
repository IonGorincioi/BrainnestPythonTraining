# Given a text string that contains words separated by whitespace,
# write a regular expression to count the number of words in the string.
import re
text = "Hello everyone! Welcome to Brainnest Python training."

# txt = "The best thigs are learnt during the worst days of your life"
p = re.compile('\w+')
n=len(p.findall(text))
print(n)