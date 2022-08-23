#this is a program to see if the number is a leap year.
year = int(input('enter the year:'))
if year%4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('this year is a leap year')
        else:print('number is not a leap year')
    else:print('number is not a leap year')
else:print('number is not a leap year')
