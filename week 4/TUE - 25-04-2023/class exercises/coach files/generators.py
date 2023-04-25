def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

x = simpleGeneratorFun()

print(next(x)) 
print(next(x))
print(next(x))


def simpleGeneratorFun():
	yield 1		
	yield 2		
	yield 3		

for value in simpleGeneratorFun():
	print(value)


def fib(limit):
    
    a, b = 0, 1

    while a < limit:
        yield a
        a, b = b, a + b

x = fib(5)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


print("\nUsing for in loop")
for i in fib(5):
    print(i)
