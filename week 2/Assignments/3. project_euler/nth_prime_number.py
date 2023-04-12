# By listing the first six prime numbers: 2, 3, 5, 7, 11,
# and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?


def primeNumber(nth):
    number = 1
    count = 0
    while count < nth:
        number += 1
        for integer in range(2, number + 1):
            if number % integer == 0:
                break
        if integer == number:
            count += 1
    return number


nth_prime = int(input("input the nth number: "))

print(f"The {nth_prime}th prime number is: {primeNumber(nth_prime)}")
