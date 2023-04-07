# Rewrite your pay computation with time-and-a-half for
# overtime and create a function called compute pay
# which takes two parameters
# (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def computepay(hours, rate):
    if hours <= 40:
        if hours <= 0:
            print("Working hours cannot be zero or less.")
        else:
            pay = hours * rate
    else:
        extraHours = hours - 40
        pay = rate * (40 + extraHours * 1.5)

    return pay


try:
    salary = computepay(-34, 10)
    print(salary)

except ValueError:
    print("Please enter only numerical values.")

except TypeError:
    print("Please make sure that the arguments are numbers")
