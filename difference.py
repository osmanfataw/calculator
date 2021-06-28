num1 = int(input("What is the first number: "))
num2 = int(input("What is the second number: "))

difference = num1 - num2
sum = num1 + num2
if num1 >= num2:
    print(difference)
elif num1 < num2:
    print(sum)
else:
    print("Invalid")