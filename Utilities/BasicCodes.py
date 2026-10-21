
# ---------- PROGRAM 1: LARGEST NUMBER ----------

def largest_number():
    print("\n=== LARGEST OF THREE NUMBERS ===")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    largest = max(a, b, c)

    print("Largest number is:", largest)


# ---------- PROGRAM 2: MULTIPLICATION TABLE ----------

def multiplication_table():
    print("\n=== MULTIPLICATION TABLE ===")

    number = int(input("Enter a number: "))

    for i in range(1, 11):
        print(f"{number} × {i} = {number * i}")


# ---------- PROGRAM 3: EVEN OR ODD ----------

def even_or_odd():
    print("\n=== EVEN OR ODD CHECKER ===")

    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print(f"{number} is Even.")
    else:
        print(f"{number} is Odd.")


# ---------- MAIN MENU ----------

def main():
    while True:
        print("\n===== BASIC PYTHON PROGRAMS =====")
        print("1. Largest of Three Numbers")
        print("2. Multiplication Table")
        print("3. Even or Odd")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        elif choice in ["1", "2", "3"]:
            try:
                if choice == "1":
                    largest_number()

                elif choice == "2":
                    multiplication_table()

                elif choice == "3":
                    even_or_odd()

            except ValueError:
                print("Invalid input! Please enter a whole number.")

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
