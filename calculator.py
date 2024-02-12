# Calculator Program
v = float(input("Enter first number:"))
y = float(input("Enter second number:"))
operator = input("Enter the operator:")
if operator == "+":
    print("The value is:", v+y)
elif operator == "-":
    print("The value is:", v-y)
elif operator == "*":
    print("The value is:", v*y)
elif operator == "/":
    print("The value is:", v/y)
else:
    print("Invalid operator")
