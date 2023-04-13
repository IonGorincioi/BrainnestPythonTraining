# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def prime_numbers(max_number):
    number = 1
    total = 2
    while number < max_number:
        number += 2
        for divisor in range(2, max_number):
            if number % divisor == 0:
                break
        if divisor == number:
            total += number
    return total


print(prime_numbers(200000))
