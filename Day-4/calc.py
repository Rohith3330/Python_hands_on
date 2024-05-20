def calculator():
    while True:
        try:
            # Accepting user inputs
            operand1 = input("Enter the first number: ")
            operand2 = input("Enter the second number: ")
            operator = input("Enter the operator (+, -, *, /): ")
            # Convert inputs to float
            num1 = float(operand1)
            num2 = float(operand2)
            # Performing the calculation
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                # Handling division by zero
                if num2 == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                result = num1 / num2
            else:
                # Handling invalid operator
                raise ValueError("Invalid operator. Please use one of the following: +, -, *, /")

            # Printing the result
            print(f"The result of {num1} {operator} {num2} is: {result}")
        
        except ValueError as ve:
            # Handling invalid number input or operator
            print(f"Error: {ve}. Please enter valid numbers and operator.")
        
        except ZeroDivisionError as zde:
            # Handling division by zero
            print(f"Error: {zde}. Please try again.")

        # Ask if the user wants to perform another calculation
        retry = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if retry != 'yes' or retry!='y':
            print("Goodbye!")
            break

# Running the calculator function
calculator()
