# while loop

x = 0
x = x + 1
print(x)

n = 5
while n > 0:
    print(n)
    n = n - 1
print('Finished!')

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
