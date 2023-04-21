# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even) n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


def sequence_terms(starting_number):
    seq = [starting_number]
    num_of_terms = 1
    while starting_number != 1:
        if starting_number % 2 == 0:
            next_term = starting_number / 2
        else:
            next_term = 3 * starting_number + 1
        next_term = starting_number = int(next_term)
        seq.append(next_term)
        num_of_terms += 1
    return seq


def max_sequence_number(sequence):
    count = 0
    for i in sequence:
        count += 1
    return count


# print(max_sequence_number(sequence_terms(27)))

number = 1
max_value = 0
dict1 = {}
while number < 1000000:
    number += 1
    sequence_length = max_sequence_number(sequence_terms(number))
    # print(seq_length)
    if sequence_length > max_value:
        max_value = sequence_length
        dict1["number"] = number
        dict1["length"] = max_value


print(f'Number {dict1["number"]} has the longest sequence: {dict1["length"]} terms')
