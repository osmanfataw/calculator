def add(x, y):
    result = x + y
    print(result)
def sub(x, y):
    result = x - y
    print(result)
def div(x, y):
    result = x / y
    print(result)
def mult(x, y):
    result = x * y
    print(result)
operation = input("What do you want me to do: ")
x = int(input("What is the first number: "))
y = int(input("What is the second number: "))
if operation == "+":
    add(x, y)
elif operation == "-":
    sub(x, y)
elif operation == "/":
    div(x, y)
elif operation == "*":
    mult(x, y)
else:
    print("Invalid input,Try Again")