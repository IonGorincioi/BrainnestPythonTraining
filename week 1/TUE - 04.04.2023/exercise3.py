# 1. Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    if hours <= 40:
        if hours <= 0:
            print("Working hours cannot be zero or less.")
        else:
            pay = hours * rate
    else:
        extraHours = hours - 40
        pay = rate * (40 + extraHours * 1.5)

    print(pay)
except ValueError:
    print("Please enter only numerical values.")


