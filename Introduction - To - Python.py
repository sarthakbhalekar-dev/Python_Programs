#How To Declare A Value To A Variable?
num1=10
num2=10.5
#In The Above Situation, Num1 Is 10 ( Integer ) , & Num2 Is 10.5 ( Float )
#While In Other Languages, We Write:- int num1 = 10 , float num2 = 10.5


#Printing The Code.
print(num1)
print(num2)


#Running The Code.
#Click Run
#Click Run Module
#Save The File
#Code Is Running In Main Tab Now.


#Printing A String.
print("The Value Stored In Num1 Is ", num1, "& Value Stored In Num2 Is", num2) 


#Printing Rules.
#To Print A Single Line:-
str1 = 'Hello World!'
#To Print A Paragraph:-
str2 = ''' Python can be easy to pick up whether
you're a first time programmer or you're
experienced with other languages.'''
print(str1)
print(str2)


#How To Use Comments.
#Just Put A Hashtag In Front Of The Sentence. It Will Become A Comment.


#How To Print A Specific Part Of Sentence?
#We Use **Slicing** :- Picking Up Characters From The String And Printing It.
snum = 'My Name Is Sarthak!'
print(snum[11])
#In Slicing, Remember This Points:-
#In The Index Ie. (snum<--- String Value[11]<--- This Is Known As Index No.), 0 Is Always The First No. (Space Is Also Counted As A Character).
print(snum[0:7])
#Always Take More 1 More Than Original No :- So 6+1 - 7
print(snum[-1])
#For Starting WIth Negative Index Ie. Starting To Count From Behind.


#List
a=[1,'S',10.5,'Hello']

#Removing An Element From List
a.remove(10.5)
print(a)

#Inserting Values In List
a.insert(2,10)
print(a)

#Tuple
x=(1,2,3,4,5)
print(x)


#How To Use Operations 2 Values.

#Modulo Operator
x=10
y=2
result=x%y
print(result)

#Floor Division
x=10
y=2
result=x//y
print(result)

#To Check Whether 1 Value Is Equal To Other One.
x=10
y=2
print(x==y)

#While Loop.
n1=1
while(n1<11):
    print(n1)
    n1+=1
#Infinite Loop In While Loop/
#num1=0
#while num1<1:
#print(num1)
    
#For Loop( How To Print Characters In Horizontal Way )
for i in 'Sarthak':
    print(i)

#One More Example
a=['Stars','Moon','Sun']
for j in a:
    print(j)

#Range
three=range(1,20,2)
for i in three:
    print(i)

#Dictionary
s={"Name":"Sarthak","Grade":"8","Dob":"25/02/2008"}
print(s["Name"])
print(s.keys())
