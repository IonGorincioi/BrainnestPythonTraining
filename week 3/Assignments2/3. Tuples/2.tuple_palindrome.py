# Write a function to check if a given tuple is a palindrome,
# meaning the elements are the same in reverse order.

def is_palindrome(iterable):
    iterable = list(iterable)
    rev_iter = list(reversed(iterable))

    if iterable == rev_iter:
        return f"{iterable} is palindrome."
    return f"{iterable} is not palindrome."


numbers = (1, 2, 3, 2, 1)
print(is_palindrome(numbers))
