one=eval(input("Enter First Value : "))
two=eval(input("Enter Second Value : "))
addition=one+two
subtract=one-two
multiply=one*two
division=one/two
print(""" Valid operations example are given e.g. 
            type add    for Addition or +
            type sub    for Subtraction or -
            type multi  for Multiplication or *
            type divide for Division or /
            
            """)
result=input("Enter Operations to perform :")
if result=='add':
    print(f" First value is {one} and Second Value is {two} and result is {addition}")
elif result=='sub':
    print(f" First value is {one} and Second Value is {two} and result is {subtract}")
elif result=='multi':
    print(f" First value is {one} and Second Value is {two} and result is {multiply}")
elif result=='divide':
    print(f" First value is {one} and Second Value is {two} and result is {division}")
else:
    print(" Please select operation")
