str1=input("Please Enter A String To Be Reversed: ") #Taking String From User
rev_str1=" " #Creating An Empty Variable To Store The Reversed Sring

for x in range(len(str1)-1,-1,-1): #Take Me Through The String From The Last Character To The First
    rev_str1+=str1[x] #Take 1 Letter At A Time From The Last Position & Add To The Empty Variable
print(rev_str1)
