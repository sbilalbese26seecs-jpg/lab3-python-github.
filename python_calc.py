#python_calc.py
# Task 1: Feature-rich calculator
# Note: Python does not need "using namespace std;" (that is C++), so it is not used here.


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # handle division by zero
    if b == 0:
        return None
    return a / b


def check_even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


def percentage(a, b):
    # percentage of a with respect to b  ->  (a / b) * 100
    if b == 0:
        return None
    return (a / b) * 100


def show_menu():
    print("\n===== Python Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")


def get_number(message):
    # keeps asking until the user enters a valid number
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "7":
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice! Please select from 1 to 7.")
            continue

        if choice == "5":
            # even/odd only needs one number, so it must be a whole number
            num = get_number("Enter a number: ")
            if num != int(num):
                print("Even/Odd check works only for whole numbers.")
            else:
                print(int(num), "is", check_even_odd(int(num)))
            continue

        # all other options need two numbers
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            print("Result:", num1, "+", num2, "=", add(num1, num2))
        elif choice == "2":
            print("Result:", num1, "-", num2, "=", subtract(num1, num2))
        elif choice == "3":
            print("Result:", num1, "x", num2, "=", multiply(num1, num2))
        elif choice == "4":
            result = divide(num1, num2)
            if result is None:
                print("Error: Division by zero is not allowed!")
            else:
                print("Result:", num1, "/", num2, "=", result)
        elif choice == "6":
            result = percentage(num1, num2)
            if result is None:
                print("Error: Cannot calculate percentage with respect to zero!")
            else:
                print(num1, "is", round(result, 2), "% of", num2)


main()
