def my_function(fname):
    print("Hello " + fname.capitalize())


my_function('Ion')
my_function('Tobias')
my_function('jonson')

print("---------------------------")


def function2(x):
    return 5 * x


print(function2(3))

print("---------------------------")


def myFun(*args):
    """ We use (*args) when we do not know
        the number of arguments."""
    for arg in args:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'class')

print("---------------------------")


def myFun2(arg1, arg2, arg3):
    print("arg1 :", arg1)
    print("arg2 :", arg2)
    print("arg3 :", arg3)


args = ("this", 'is', 'demo')
# myFun2(args)
myFun2(*args)

