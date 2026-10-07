#Input three number and print the largest of three numbers using if statement:
a=int(input("Enter a number "))
b=int(input("Enter a number "))
c=int(input("Enter a number "))
larg=a
if b>larg:
    larb=b
if c>larg:
    larg=c
print("Largest of all is ",larg)

#Input a number and print the table of a tabular form.
num=int(input("Enter a number "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)


#Input a number and check whether the number is even or odd.
num=int(input("Enter a Number"))
if num%2==0:
    
              print("number is even")
else:
              print("number is odd")
