
import re
# txt = 'Hello, How are you? aHHH'
# print(re.findall(r'H', txt)) # matches any 'H'
# print(re.findall(r'\bH', txt)) # matches any 'H' on word boundary
# print(re.findall(r'^H', txt)) # matches only 'H' onstart of string

pattern = re.compile(r'[?:(https?|s?ftp):\/\/)?]+[?:www\.?]{4}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}')
print(pattern.search('http://www.example.com/questions/3456/my-document'))