# Given a list of numbers, write a function to
# return a set of all prime numbers from the list.


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


def convert_list_to_set(the_list):
    primes = []

    for item in the_list:
        for divisor in range(2, item + 1):
            if item % divisor == 0:
                break

        if divisor == item:
            primes.append(item)

        divisor += 1
    return set(primes)


print(convert_list_to_set(numbers))
