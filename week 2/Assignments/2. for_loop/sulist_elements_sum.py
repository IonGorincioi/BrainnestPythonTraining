# Create a for loop that iterates through a list of lists
# and prints the sum of the elements in each sub-list.

number_lists = [[2, 5, 8, 12],
                [8, 4, 3, 16],
                [9, 2, 18, 1, 5, 13],
                [12, 4, 32, 9, 10]]

for sublist in number_lists:
    the_sum = sum(sublist)
    print(the_sum)

