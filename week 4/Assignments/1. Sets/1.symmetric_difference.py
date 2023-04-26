# Given two sets A and B, write a function to return
# the symmetric difference between them as a new set.
# The symmetric difference is the set of elements
# that are in either A or B, but not in both.

def sym_dif(s1, s2):
    result = s1.symmetric_difference(s2)
    return result


set1 = {"javascript", "python", "C#", "C++"}
set2 = {"html", "css", "javascript", 'C#'}

symmetricDifference = sym_dif(set1, set2)
print(symmetricDifference)