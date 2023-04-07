# Write a program to prompt for a score between 0.0 and
# 1.0. If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0, print a grade using
# the following table:

# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F


def grade(score):
    if score >= 0.9:
        print(f"Your grade is: A \nExcelent result!")
    elif score < 0.9 and score >= 0.8:
        print(f"Your grade is: B\nCongratulation!")
    elif score < 0.8 and score >= 0.7:
        print(f"Your grade is: C\nWell done!.")
    elif score < 0.7 and score >= 0.6:
        print(f"Your grade is: D\nGood result!")
    elif score < 0.6:
        print(f"Your grade is: F\nUnfortunately you didn't pass.")
    else:
        print('Please make sure the score is between 0 and 1')


user_input = int(input("Enter a number between 0 and 1: "))
grade(user_input)
