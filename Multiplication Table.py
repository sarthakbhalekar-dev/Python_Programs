# 2. Create a program that accepts a number and then prints a table for that number.

number = int(input ("Enter a Number: "))
print ("The Multiplication Table of: ", number)

for count in range(1, 11):      
   print (number, 'x', count, '=', number * count)  
