import math
def calculator():
    print(" Calculator App")
    print("Type 'exit' if you want to quit.")
    
    while True:
        
        num1 = input("Enter the first number: ")
        if num1.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        
        operator = input("Enter an operator (+, -, *, /): ")
        if operator.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        
        num2 = input("Enter the second number: ")
        if num2.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        try:
            num1 = float(num1)
            num2 = float(num2)

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator. Use +, -, *, or /.")
                continue

            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
