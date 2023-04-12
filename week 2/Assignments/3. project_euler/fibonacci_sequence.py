# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

def Fibonacci():
    fib = [1, 2]
    end_of_sequence = False
    while not end_of_sequence:
        for index in range(len(fib)):
            next_num = fib[index - 1] + fib[index]
            if next_num > 4000000:
                end_of_sequence = True
        fib.append(next_num)
    return fib


def total_even_fib(fibonacci):
    fib_even = []
    for number in fibonacci:
        if number % 2 == 0:
            fib_even.append(number)
            even_total = sum(fib_even)

    return even_total


print(f"Total of fibonacci even numbers: ", total_even_fib(Fibonacci()))
