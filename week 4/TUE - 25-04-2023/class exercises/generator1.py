# Write a generator function that takes a list of
# numbers as input and yields only the even numbers.

numbers = [3, 4, 32, 65, 8, 18, 24]

def even_numbers(list_of_numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number

evens = even_numbers(numbers)
print(next(evens))
#

#
# def even_numbers(nums):
#     for num in nums:
#         if num % 2 == 0:
#             yield num
#
#
# my_list = [x for x in range(50)]
#
# even_nums = even_numbers(my_list)
#
# for num in even_nums:
#     print(num)
