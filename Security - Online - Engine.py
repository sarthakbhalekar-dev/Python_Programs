user_pin=2827
user_name="Sarthak"
enter_name=str(input("Please Enter Your UserName: "))
enter_pin=int(input("Please Enter Your Pin: "))
if (user_name == enter_name):
    print("UserName Verified SuccessFully.")
else:
    print("UserNamee InValid! Please Try Again! ")
if (user_pin == enter_pin):
    print("Pin Is Correct.")
    print("Logged In Successfully.")
else:
    print("Pin Is Incorrect! Try Again!")



              
