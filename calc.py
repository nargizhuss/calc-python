

what = input( "What do you want to do? :" )

a = float (input( "enter first integer: " ))
b = float (input( "enter second integer: " ))

if what == "+":
    c = a + b
    print("Your total is: " + str(c))

elif what == "-":
    c = a - b
    print("Your total is: " + str(c))

elif what == "*":
   c = a * b
   print("Your total is: " + str(c))

elif what == "/":
   c = a / b
   print("Your total is: " + str(c))

elif what == "//":
   c = a // b
   print("Your total is: " + str(c))

elif what == "**":
    c = a ** b
    print("Your total is: " + str(c))

elif what == "%":
    c = a % b
    print("Your total is: " + str(c))

else:
   print( "Error has occured.." )

input()