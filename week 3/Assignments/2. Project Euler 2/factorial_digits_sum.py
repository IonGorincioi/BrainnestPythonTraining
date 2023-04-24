def compute_factorial(number):
    """ takes a number and calculates the factorial of that number """
    factorial = number
    for i in range(1, number):
        factorial = factorial * (number - i)
    return factorial


factorial_of_number = compute_factorial(100)

digits_sum = 0
while factorial_of_number > 0:
    digit = factorial_of_number % 10
    digits_sum += digit
    factorial_of_number //= 10

print(digits_sum)