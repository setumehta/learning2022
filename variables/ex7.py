# program to swap variables without using extra variable.

a = int(input("enter the value of a = "))
b = int(input('enter the value of b = '))
a = a + b
b = a - b
a = a - b

print('the value of a is ',a,'value of b is ',b)