def calculator():
    print("--- Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Operations: + (Add), - (Subtract), * (Multiply), / (Divide)")
        operation = input("Choose an operation: ")

        if operation == '+':
            print(f"Result: {num1 + num2}")
        elif operation == '-':
            print(f"Result: {num1 - num2}")
        elif operation == '*':
            print(f"Result: {num1 * num2}")
        elif operation == '/':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation choice.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
