# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are
# 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand)
# inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example,
# 342 (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and"
# when writing out numbers is in compliance with British usage.

import re


def number_spelled(number: int) -> int:
    digit_dict = {0: "zero",
                  1: "one",
                  2: "two",
                  3: "three",
                  4: "four",
                  5: "five",
                  6: "six",
                  7: "seven",
                  8: "eight",
                  9: "nine",
                  10: "ten",
                  11: "eleven",
                  12: "twelve",
                  13: "thirteen",
                  14: "fourteen",
                  15: "fifteen",
                  16: "sixteen",
                  17: "seventeen",
                  18: "eighteen",
                  19: "nineteen",
                  20: "twenty",
                  30: "thirty",
                  40: "forty",
                  50: "fifty",
                  60: "sixty",
                  70: "seventy",
                  80: "eighty",
                  90: "ninety",
                  1000: "onethousand"}
    # if the number is a special case present in the dictionary
    # the length of the value will be displayed
    if number in digit_dict:
        return len(digit_dict[number])

    # split the digits of the number and add them in a list 432 --> [4,3,2]
    digits = []

    while number > 0:
        digits.insert(0, number % 10)
        number //= 10
    output = []
    # take the digits list and return them in words
    for i in range(len(digits)):
        digit = digits[i]

        if digit == 0:
            continue

        # check the place value of each digit
        if len(digits) - i == 3:  # Hundreds
            output.append(digit_dict[digit])
            output.append("hundred")
            output.append("and")
        elif len(digits) - i == 2:  # Tens
            if digit >= 2:
                output.append(digit_dict[digit * 10])
            else:
                output.append(digit_dict[10 + digits[i + 1]])
                break
        else:  # Units
            output.append(digit_dict[digit])
    if output[-1] == "and":
        output.pop(-1)

    return len(''.join(output))


total = 0
for i in range(1, 1001):
    total += number_spelled(i)
print(total)
