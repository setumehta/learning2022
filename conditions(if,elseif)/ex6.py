# program to count the grades of a student.
a = int(input('enter the marks :'))
b = int(input('enter the marks :'))
c = int(input('enter the marks :'))
if a >= 0 and a <= 100 and b >= 0 and b <= 100 and c >=0 and c <=100:
    average = (a+b+c)/3
    print('average marks are ',average)

    if average >= 90 and average <= 100:
        print('ceo')
    elif average >= 80 and average <= 89:
        print('executive')
    elif average >= 70 and average <= 79:
        print('manager')
    elif average >= 60 and average <= 69:
        print('peon')
    elif average >= 0 and average <= 59:
        print('politician')
else:
    print('marks check kar chodiya')