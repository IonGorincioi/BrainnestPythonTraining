# Given a list of sets, write a function to return
# the Cartesian product of all sets in the list.
sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]


def cartesian_product(list_of_sets):
    cartesian = []
    for single_set in sets:
        single_set = list(single_set)

        print(single_set)


cartesian_product(sets)
