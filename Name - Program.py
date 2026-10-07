first_name = input ("Please Enter Your First Name : ")
middle_name = input ("Please Enter Your Middle Name(Or Else Type None.): ")
last_name = input ("Please Enter Your Last Name : ")

if (middle_name == 'None'):
    print('Your Full Name Is '+ first_name+' '+middle_name+' '+last_name)
else:
    print('Your Full Name Is '+first_name+' '+last_name)
