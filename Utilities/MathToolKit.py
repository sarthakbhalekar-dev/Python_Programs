
import math


# ---------- INPUT HELPERS ----------

def get_number(message):
    while True:
        try:
            number = float(input(message))

            if math.isfinite(number):
                return number

            print("Please enter a finite number.")

        except ValueError:
            print("Invalid input! Enter a number.")


def get_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a whole number.")


# ---------- 1. CALCULATOR ----------

def calculator():
    print("\n=== BASIC CALCULATOR ===")

    a = get_number("First number: ")
    b = get_number("Second number: ")

    print(f"\nAddition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")

    if b == 0:
        print("Cannot divide by zero!")
    else:
        print(f"Division: {a / b}")
        print(f"Modulo: {a % b}")
        print(f"Floor Division: {a // b}")


# ---------- 2. MULTIPLICATION TABLE ----------

def multiplication_table():
    print("\n=== MULTIPLICATION TABLE ===")

    number = get_integer("Enter number: ")

    limit_text = input(
        "Enter upper limit (default 10): "
    ).strip()

    if limit_text == "":
        limit = 10
    else:
        try:
            limit = int(limit_text)
        except ValueError:
            print("Invalid limit. Using 10.")
            limit = 10

    if limit < 1:
        print("Limit must be positive.")
        return

    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")


# ---------- 3. EVEN OR ODD ----------

def even_odd():
    print("\n=== EVEN OR ODD ===")

    number = get_integer("Enter a whole number: ")

    if number % 2 == 0:
        print(f"{number} is EVEN.")
    else:
        print(f"{number} is ODD.")


# ---------- 4. AREA AND PERIMETER ----------

def area_perimeter():
    print("\n=== AREA AND PERIMETER ===")

    length = get_number("Enter length: ")

    width_text = input(
        "Enter width (Enter for square): "
    ).strip()

    if width_text == "":
        width = length
    else:
        try:
            width = float(width_text)
        except ValueError:
            print("Invalid width!")
            return

    if (
        not math.isfinite(width)
        or length <= 0
        or width <= 0
    ):
        print("Dimensions must be positive finite numbers.")
        return

    area = length * width
    perimeter = 2 * (length + width)

    shape = "Square" if length == width else "Rectangle"

    print(f"\nShape: {shape}")
    print(f"Area: {area:.2f}")
    print(f"Perimeter: {perimeter:.2f}")


# ---------- 5. PRIME OR COMPOSITE ----------

def prime_checker():
    print("\n=== PRIME OR COMPOSITE ===")

    number = get_integer("Enter an integer: ")

    if number <= 1:
        print("Neither prime nor composite.")
        return

    is_prime = True

    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is PRIME.")
    else:
        print(f"{number} is COMPOSITE.")


# ---------- 6. SQUARE ROOT ----------

def square_root():
    print("\n=== SQUARE ROOT ===")

    number = get_number("Enter number: ")

    if number < 0:
        print("Negative numbers have complex square roots.")
    else:
        print(f"Square root: {math.sqrt(number):.4f}")


# ---------- 7. TEMPERATURE CONVERTER ----------

def temperature_converter():
    print("\n=== TEMPERATURE CONVERTER ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        celsius = get_number("Enter Celsius: ")
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius}°C = {fahrenheit:.2f}°F")

    elif choice == "2":
        fahrenheit = get_number("Enter Fahrenheit: ")
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit}°F = {celsius:.2f}°C")

    else:
        print("Invalid choice!")


# ---------- 8. CURRENCY CONVERTER ----------

def currency_converter():
    print("\n=== CURRENCY CONVERTER ===")
    print("Educational example rates only.")
    print("These are NOT live exchange rates.\n")

    print("Base Currency:")
    print("1. Indian Rupee (INR)")
    print("2. US Dollar (USD)")

    base = input("Choose base (1-2): ").strip()

    print("\nTarget Currency:")
    print("1. Euro (EUR)")
    print("2. Chinese Yuan (CNY)")
    print("3. UAE Dirham (AED)")

    target = input("Choose target (1-3): ").strip()

    rates = {
        "1": {
            "1": (0.011, "EUR"),
            "2": (0.087, "CNY"),
            "3": (0.049, "AED")
        },
        "2": {
            "1": (0.82, "EUR"),
            "2": (6.44, "CNY"),
            "3": (3.67, "AED")
        }
    }

    if base not in rates or target not in rates[base]:
        print("Invalid currency selection!")
        return

    amount = get_number("Enter amount: ")

    if amount < 0:
        print("Amount cannot be negative.")
        return

    rate, currency = rates[base][target]
    converted = amount * rate

    print(f"\nConverted amount: {converted:.2f} {currency}")
    print("Note: Example rates, not suitable for transactions.")


# ---------- 9. COMPARE NUMBERS ----------

def compare_numbers():
    print("\n=== COMPARE TWO NUMBERS ===")

    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    if a > b:
        print(f"{a} is greater than {b}.")

    elif a < b:
        print(f"{a} is smaller than {b}.")

    else:
        print("Both numbers are equal.")


# ---------- MAIN MENU ----------

def math_menu():
    tools = {
        "1": calculator,
        "2": multiplication_table,
        "3": even_odd,
        "4": area_perimeter,
        "5": prime_checker,
        "6": square_root,
        "7": temperature_converter,
        "8": currency_converter,
        "9": compare_numbers
    }

    while True:
        print("\n" + "=" * 36)
        print("          MATH TOOLKIT HUB")
        print("=" * 36)

        print("1. Basic Calculator")
        print("2. Multiplication Table")
        print("3. Even / Odd")
        print("4. Area & Perimeter")
        print("5. Prime / Composite Check")
        print("6. Square Root")
        print("7. Temperature Converter")
        print("8. Currency Converter")
        print("9. Compare Two Numbers")
        print("0. Exit")

        print("=" * 36)

        choice = input("\nSelect an option (0-9): ").strip()

        if choice == "0":
            print("\nThanks for using Math Toolkit Hub!")
            break

        elif choice in tools:
            try:
                tools[choice]()

            except (OverflowError, ZeroDivisionError):
                print("Calculation error: number is too large.")

            input("\nPress Enter to return to menu...")

        else:
            print("Invalid option! Please try again.")


# ---------- START ----------

if __name__ == "__main__":
    math_menu()
