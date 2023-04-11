# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples(number, factor1, factor2):
    # total = 0
    multiple_list = []
    for num in range(1, number):
        if num % factor1 == 0 or num % factor2 == 0:
            multiple_list.append(num)
            total = sum(multiple_list)
    print(f"The sum of multiples of {factor1} and {factor2} bellow {number} is '{total}'.")


multiples(10, 3, 5)
multiples(100, 3, 5)
multiples(1000, 3, 5)

