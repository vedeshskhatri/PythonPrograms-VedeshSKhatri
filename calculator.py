# Simple Calculator Program in Python

def add(x, y):
    return x + y #adds the given value

def subtract(x, y):
    return x - y #subtracts the given value

def multiply(x, y):
    return x * y #multilpilies the given value

def divide(x, y):
    if y == 0: #divides the given value
        return "Error: Cannot divide by zero"
    return x / y

print("Select operation:") #opeartion selection
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid input")

except ValueError:
    print("Error: Please enter valid numbers")
