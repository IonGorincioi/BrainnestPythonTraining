# .Write a list comprehension to find all the numbers between
# 1 and 1000 that are divisible by 7 but not by 5.

numbers = [num for num in range(1000) if num % 7 == 0 and num % 5 != 0]
print(numbers)
