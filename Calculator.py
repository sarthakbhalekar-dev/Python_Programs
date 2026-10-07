num1=int(input("Enter The First Number: "))
num2=int(input("Enter The Second Number: "))
print("1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division \n 5.Modulo \n 6.Floor Division")
choice=int(input("Select Your Choice!"))

if (choice==1):
    print(num1+num2)
if (choice==2):
    print(num1-num2)
if (choice==3):
    print(num1*num2)
if (choice==4):
    print(num1/num2)
if (choice==5):
    print(num1%num2)
if (choice==6):
    print(num1//num2)
