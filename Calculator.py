# python calculator

operator = input("Enter the operator (+ - * / )")
n1 = float(input("E$nter the first number"))
n2 = float(input("enter the Secont number"))

if operator == "+":
    print(n1 +n2)
elif operator == "-":
    print(n1-n2)
elif operator == "*":
    print(n1*n2)
else:
    print(n1/n2)