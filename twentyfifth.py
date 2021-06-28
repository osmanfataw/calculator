def addition(x, y):
    result = x + y
    print("The sum of x and y is ",result)
    
    
def subtract(x, y):
    result = x - y
    print("The difference of x and y is ",result)
    
    
def divide(x, y):
    result = x / y
    print("The result of x and y is ",result)
    
    
def multiply(x, y):
    result = x * y
    print("The product of x and y is ",result)
    
prompt = input("What is the mode of operation: ")
x = int(input("What is the first number: "))
y = int(input("What is the second number: "))

if prompt == "+":
    addition(x, y)
elif prompt == "-":
    subtract(x, y)
elif prompt == "/":
    divide(x, y)
elif prompt == "*":
    multiply(x, y)
else:
    print("Wrong mode of operation")