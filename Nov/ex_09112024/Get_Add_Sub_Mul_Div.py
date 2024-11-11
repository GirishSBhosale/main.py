# Program published on https://beginnersbook.com

# Task 3 - Addition Subtraction Multiplication and Division of two numbers

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = input("Enter operation as given+,-,*,/: ")

result = 0
if num3 == '+':
    result = num1 + num2
elif num3 == '-':
    result = num1 - num2
elif num3 == '*':
    result = num1 * num2
elif num3 == '/':
    result = num1 / num2
else:
    print("Input character is invalid!")

print(num1, num3 , num2, ":", result)