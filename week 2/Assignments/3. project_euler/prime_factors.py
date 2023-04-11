# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def factorisation(number):
    divisor = 2
    prime_factors = []
    while divisor ** 2 <= number:
        if number % divisor != 0:
            divisor += 1
        else:
            number = number // divisor
            prime_factors.append(divisor)
    if number > 1:
        prime_factors.append(number)
    return prime_factors

print(factorisation(37))
print(factorisation(13195))
print(factorisation(600851475143))

