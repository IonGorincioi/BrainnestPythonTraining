# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012 021 102 120 201 210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def digits_of_the_number(number):
    number_digits = []
    while number > 0:
        digit = int(number) % 10
        number_digits.insert(0, digit)
        number //= 10
    return number_digits


def all_permutations(the_list):
    permutations = []

    # if the list contains only one item, the actual list will be returned
    if len(the_list) == 1:
        return [the_list]

    for index in range(len(the_list)):
        perm = the_list[index]
        new_list = the_list[:index] + the_list[index + 1:]

        # print(new_list)
        for p in all_permutations(new_list):
            permutations.append([perm] + p)
    return permutations


list_of_digits = digits_of_the_number(102)
# print(list_of_digits)

permutation_list = all_permutations(list_of_digits)
# print(permutation_list)

print(sorted(permutation_list))
