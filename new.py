def add(a, b):
    result = a + b
    print("The result is ", result)
def sub(a, b):
    result = a - b
    print("The result is ", result)
def div(a, b):
    result = a / b
    print("The result is ", result)
def multiply(a, b):
    result = a * b
    print("The result is ", result)

operator = input("Please select operator: ")
a = int(input("What is the first number: "))
b = int(input("What is the second number: "))
if operator == "+":
    add(a, b)
elif operator == "-":
    sub(a, b)
elif operator == "/":
    div(a, b)
elif operator == "*":
    multiply(a, b)
else:
    print("Invalid input, please try again")