def calculate_grade(score):
    # Determine the corresponding letter grade based on the score
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    # Prompt the user to enter a numeric score
    while True:
        try:
            score = float(input("Enter the numeric score (between 0 and 100): "))
            if 0 <= score <= 100:
                break
            else:
                print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric score.")

    # Calculate the corresponding letter grade
    grade = calculate_grade(score)

    # Display the numeric score and corresponding letter grade
    print("Numeric Score: {:.2f}".format(score))
    print("Letter Grade: {}".format(grade))

if __name__ == "__main__":
    main()
