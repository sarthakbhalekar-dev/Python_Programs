user_pin = 1234
user_name = "Sarthak"

enter_name = input("Please Enter Your Username: ").strip()

if enter_name == user_name:
    print("Username Verified Successfully.")
    
    enter_pin = int(input("Please Enter Your PIN: "))
    
    if enter_pin == user_pin:
        print("PIN Is Correct.")
        print("Logged In Successfully!")
    else:
        print("PIN Is Incorrect! Access Denied.")
else:
    print("Username Invalid! Please Try Again.")