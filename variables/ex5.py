# this program lets the user to input seconds and shows minutes,hours and seconds as output.
seconds = int(input("please enter seconds = "))
print("hours = ",int(seconds/3600))
print("minutes ",int((seconds%3600)/60))
print("seconds",int(seconds%3600))