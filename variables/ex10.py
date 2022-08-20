# this is a program to calculate compound interest.

principle = int(input('enter the principle amount'))
rate = int(input("enter the rate "))
time = int(input("enter the time "))
ci = int(principle *(1 +rate/100)**time -principle)
print('compound interest of the given principle ,rate and time is :',ci)