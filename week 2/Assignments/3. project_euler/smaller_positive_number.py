# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_number_multiples(highest_divisor):

    number = highest_divisor

    solution_not_found = True
    while solution_not_found:

        for divisor in range(1, highest_divisor + 1):

            # divide potential solution to all numbers from 1 to highest_divisor
            if number % divisor == 0:
                if divisor == highest_divisor:
                    solution = number
                    solution_not_found = False
            else:
                break
        number += 1

    return solution


print(f"The result is: {smallest_number_multiples(20)}")
