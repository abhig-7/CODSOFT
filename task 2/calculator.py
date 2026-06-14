# Simple Calculator Using Loop

while True:
    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Thank you for using the calculator!")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2
                print(f"Result = {result}")

            elif choice == "2":
                result = num1 - num2
                print(f"Result = {result}")

            elif choice == "3":
                result = num1 * num2
                print(f"Result = {result}")

            elif choice == "4":
                if num2 != 0:
                    result = num1 / num2
                    print(f"Result = {result}")
                else:
                    print("Error: Division by zero is not allowed.")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

    else:
        print("Invalid choice! Please try again.")