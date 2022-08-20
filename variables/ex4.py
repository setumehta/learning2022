#this is a program to calculate simple interest.
principle = int(input("enter principle amount "))
rate = int(input("enter rate of interest "))
time = int(input("enter time period in years "))

print("simple interest is",(principle*rate*time)/100)