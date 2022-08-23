# program to find the day.

number = int(input('enter a number:'))

if number >= 1 and number <=7:
    if number == 1:
        print('monday')
    elif number == 2:
        print('tuesday')
    elif number == 3:
        print('wed')
    elif number == 4:
        print('thursday')
    elif number == 5:
        print('fri')
    elif number == 6:
        print('sat')
    else:
        print('sun')
else: print('invalid input')