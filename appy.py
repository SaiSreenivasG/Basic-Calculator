from helpers import *
n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))
print("Select the operation to do on the two numbers")
print("Type 1 - Multiplication")
print("Type 2 - Addition")
print("Type 3 - Divide")
print("Type 4 - subtraction")
print("Type 5 - power/exponential")
operator = int(input("Enter the option from above"))

if operator == 1:
    print(multiply(n1,n2))
elif operator == 2:
    print(add(n1,n2))
elif operator == 3:
    print(divide(n1,n2))
elif operator == 4:
    print(sub(n1,n2))
elif operator == 5:
    print(power(n1,n2))
else:
    print("Please select valid option")



