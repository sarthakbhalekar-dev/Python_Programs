str_1="My Name Is Sarthak."

s=""

#This For Loop Reduces The String To Letters, Numbers & Spaxes.
for char in str_1:
    if char.isalnum() or char.isspace() or char == "-":
        s+=char

words=s.split()
n = len(words)      

print(words)
print(n)
