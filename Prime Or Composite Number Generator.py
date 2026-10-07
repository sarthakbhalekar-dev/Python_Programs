n1=int(input("Enter A Number: "))
print("Number Given By User: ", n1)
check=2
count=0
if n1==2:
    print("It Is A Prime Number!")

while check<n1:
    r=n1%check
    if r!=0:
        check+=1
    elif r==0:
        count=1
        check+=1
if count==1:
    print("It Is A Composite Number!")
elif count==0:
    print("It Is A Prime Number!")
