def apply_operator(total_value, operator, *numbers):
    result = total_value
    if operator == '+':
        for num in numbers:
            result += num
    elif operator == '-':
        for num in numbers:
            result -= num
    else:
        print("Invalid operator. Please use '+' or '-'.")
        return None
    return result

def main():
    try:
        total_value = float(input("Enter the total value: "))
        operator = input("Enter the operator (+ or -): ")
        numbers = []
        while True:
            num = input("Enter a number (or leave empty to finish): ")
            if num == "":
                break
            numbers.append(float(num))
        result = apply_operator(total_value, operator, *numbers)
        if result is not None:
            print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
