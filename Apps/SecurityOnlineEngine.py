
import getpass

# Login details (for practice only)
username = "Sarthak"
pin = "1234"

attempts = 3

print("===== LOGIN SYSTEM =====")

while attempts > 0:
    enter_name = input("Enter Username: ").strip()
    enter_pin = getpass.getpass("Enter PIN: ")

    if enter_name.lower() == username.lower() and enter_pin == pin:
        print("\nUsername and PIN verified!")
        print("Login Successful! Welcome,", username)
        break

    else:
        attempts -= 1
        print("\nIncorrect username or PIN.")

        if attempts > 0:
            print("Attempts remaining:", attempts)
        else:
            print("Access Denied! Too many attempts.")

print("===== SESSION ENDED =====")
