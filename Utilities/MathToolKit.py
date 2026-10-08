import math


def math_menu():
    while True:
        print("\n==============================")
        print("       MATH TOOLKIT HUB       ")
        print("==============================")
        print("1. Basic Calculator (+, -, *, /, %, //)")
        print("2. Multiplication Table")
        print("3. Check Even / Odd")
        print("4. Area & Perimeter (Rectangle / Square)")
        print("5. Prime / Composite Check")
        print("6. Square Root")
        print("7. Temperature Converter (C to F)")
        print("8. Currency Converter")
        print("9. Compare Two Numbers (Greater / Smaller / Equal)")
        print("0. Exit")
        print("==============================")

        choice = input("\nSelect an option (0-9): ").strip()

        # 1. Basic Calculator
        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"\n--- Results ---")
            print(f"Addition:       {a + b}")
            print(f"Subtraction:    {a - b}")
            print(f"Multiplication: {a * b}")
            if b != 0:
                print(f"Division:       {a / b}")
                print(f"Modulo:         {a % b}")
                print(f"Floor Division: {a // b}")
            else:
                print("Division / Modulo / Floor Div: Error (Cannot divide by zero)")

        # 2. Multiplication Table
        elif choice == "2":
            num = int(input("Enter number: "))
            limit = input("Enter upper limit (default 10): ").strip()
            limit = int(limit) if limit.isdigit() else 10
            
            print(f"\n--- Multiplication Table for {num} ---")
            for i in range(1, limit + 1):
                print(f"{num} x {i} = {num * i}")

        # 3. Even / Odd
        elif choice == "3":
            num = int(input("Enter a whole number: "))
            if num % 2 == 0:
                print(f"{num} is EVEN.")
            else:
                print(f"{num} is ODD.")

        # 4. Area & Perimeter
        elif choice == "4":
            l = float(input("Enter length (or side for square): "))
            w = float(input("Enter width (press enter if it's a square): ") or l)
            area = l * w
            perimeter = 2 * (l + w)
            shape = "Square" if l == w else "Rectangle"
            print(f"\n--- {shape} Results ---")
            print(f"Area: {area}")
            print(f"Perimeter: {perimeter}")

        # 5. Prime / Composite
        elif choice == "5":
            num = int(input("Enter a positive integer: "))
            if num <= 1:
                print(f"{num} is neither Prime nor Composite.")
            else:
                is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
                if is_prime:
                    print(f"{num} is a PRIME number.")
                else:
                    print(f"{num} is a COMPOSITE number.")

        # 6. Square Root
        elif choice == "6":
            num = float(input("Enter number: "))
            if num < 0:
                print("Square root of negative numbers requires complex math!")
            else:
                print(f"Square Root of {num} is {math.sqrt(num)}")

        # 7. Temperature Converter
        elif choice == "7":
            c = float(input("Enter temperature in Celsius: "))
            f = (c * 9/5) + 32
            print(f"{c}°C is equal to {f:.2f}°F")

        # 8. Currency Converter (Merged from Currency - Converter.py)
        elif choice == "8":
            print("\nBase Currency:")
            print("1. Indian Rupee (INR)")
            print("2. US Dollar (USD)")
            base = input("Select Base (1-2): ").strip()
            
            print("\nTarget Currency:")
            print("1. Euros (EUR)")
            print("2. Chinese Yuan (CNY)")
            print("3. UAE Dirham (AED)")
            target = input("Select Target (1-3): ").strip()
            
            amount = float(input("Enter Amount: "))
            
            rates = {
                "1": {"1": (0.011, "€"), "2": (0.087, "¥"), "3": (0.049, "AED ")},
                "2": {"1": (0.82, "€"),  "2": (6.44, "¥"),  "3": (3.67, "AED ")}
            }
            
            if base in rates and target in rates[base]:
                rate, symbol = rates[base][target]
                converted = amount * rate
                print(f"Converted Amount: {symbol}{converted:.2f}")
            else:
                print("Invalid currency selection!")

        # 9. Compare Numbers (Merged from Number - Greater, Smaller Or Equal.py)
        elif choice == "9":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))