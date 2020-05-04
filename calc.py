#Simple Calculator

#Mathmatic functions

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

#Display

print("Perform simple calculations, please choose one of the following:")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

choice = input("Enter your choice [1|2|3|4]: ")

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", sub(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", mult(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", div(num1, num2))

else:
    print("Invalid Entry.")