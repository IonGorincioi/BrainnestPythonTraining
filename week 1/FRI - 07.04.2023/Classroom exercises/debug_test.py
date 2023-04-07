# problem
# print('Good morning!')
# print('How are you feeling?')
# feeling = input()
#
#
# print('I am happy to hear that you are feeling ' + feeling + '.')
# print('Good afternoon!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')
# print('Good evening!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')
#


def askFeeling(timeOfDay):
    print('Good ' + timeOfDay + '!')
    print('How are you feeling?')
    feeling = input()
    print('I am happy to hear that you are feeling ' + feeling + '.')


for timeOfDay in ['morning', 'afternoon', 'evening']:
    askFeeling(timeOfDay)

print('Good morning!')
feeling = input('How are you feeling? ')
