# Write a lambda function that takes two lists of integers
# and returns a new list with the maximum value for each index
# of the two lists. For example, given [1, 3, 5] and [2, 4, 6],
# the function should return [2, 4, 6].

list1 = [1, 3, 5]
list2 = [2, 4, 6]
result = list(map(lambda x, y: max(x, y), list1, list2))
print(result)