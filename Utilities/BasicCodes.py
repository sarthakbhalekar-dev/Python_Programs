# 1. Input three numbers and print the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

larg = a
if b > larg:
    larg = b  # Fixed typo here (was 'larb')
if c > larg:
    larg = c

print("Largest of all is", larg)


# 2. Input a number and print its multiplication table
num = int(input("Enter a number: "))

for i in range(1, 11):
    # Used f-string formatting for cleaner output
    print(f"{num} * {i} = {num * i}")


# 3. Input a number and check whether the number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")