def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    while True:
        # Get user input
        operation = input("Enter operation (1-5): ")

        # Check for Quit option
        if operation == "5":
            print("Goodbye!")
            break

        # If not Quit, get numbers and perform calculation
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == "1":
            result = add(num1, num2)
        elif operation == "2":
            result = subtract(num1, num2)
        elif operation == "3":
            result = multiply(num1, num2)
        elif operation == "4":
            result = divide(num1, num2)
        else:
            result = "Invalid operation"

        # Display the result
        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
