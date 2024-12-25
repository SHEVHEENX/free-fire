def calculator():
    while True:
        print("\nSelect an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")

        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue

            if choice == '1':
                print(f"Result: {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice.")

        again = input("Do you want to perform another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    calculator()