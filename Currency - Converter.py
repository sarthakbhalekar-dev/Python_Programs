user=int(input("""Select The Currency Type:
1.The Indian Rupee(Inr)- Press 1
2.United States Dollars(Usd)- Press 2
Enter Your Choice: """))
converted=int(input("""Select The Exchange The Currency Type:
1. Euros - Press 1
2.Chinease Yuan - Press 2
3.Uae Dhirham - Press 3
Enter Your Choice: """))
amount=int(input("Enter The Amount To Be Converted: "))

if user==1:
    if converted==1:
        print("The Converted Amount Is: ", amount*0.011)
    if converted==2:
        print("The Converted Amount Is: ", amount*0.087)
    if converted==3:
        print("The Converted Amount Is: ", amount*0.049)

if user==2:
    if converted==1:
        print("The Converted Amount Is: ", amount*0.82)
    if converted==2:
        print("The Converted Amount Is: ", amount*6.44)
    if converted==3:
        print("The Converted Amount Is: ", amount*3.67)
