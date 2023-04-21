# Write a lambda function that takes a string of words separated
# by spaces, and returns a new string with the words in reverse order.
# For example, given the string "the quick brown fox",
# the function should return "fox brown quick the".

s = "the quick brown fox"
result = " ".join(reversed(s.split()))
print(result)