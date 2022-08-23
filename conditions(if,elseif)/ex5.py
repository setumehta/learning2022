#program to count telephone charges.
#conditions - 1)minimum 200 for upto 100
#              2) plus rs.0.60 per call for next 50 calls.
#               3) plus rs.0.50 per call for next 50 calls.
#               4) plus rs. 0.40 per calls beyond 200 calls.

calls = int(input('enter the number of calls :'))

if calls <= 100:
    print('charges are 200')
elif calls > 100 and calls <= 150:
    a = calls-100
    charges = (a * 0.60) + 200
    print('charges are ',charges)
elif calls > 150 and calls <= 200:
    a= calls-150
    charges = 200 +(50*.60) + (a*.50)
    print('charges are:',charges)
else:
    a = calls - 200
    charges = 200 + (50*.60) + (50 * .50) + (a * .40)
    print("charges are:",charges)
