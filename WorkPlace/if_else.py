#if_else
a=10
b=20
if a>b:
    print("b is greater")
else:
    print("a is greater") 


#if_elif_else
a=20
b=10
if a<b:
    print('b is greater')
elif a==b:
    print("a is equal b")
else:
    print("a is greater") 

#Nested if else
num=-15
if num>=0:
    if num == 0:
        print("zero")
    else:
        print("positive number")
else:
    print("negative number")



#for loop
days = ["sun","mon","tue","wed","thu","fri","sat"]
for x in days:
    print(x)            


#range(starting point,end point,interval)
    
for x in range(10):
    print(x)

a=list(range(0,15,2))
print(a) 


b=list(range(20,9,-1))
print(b)


#take input from user

first = int(input("enter first number"))
second = int(input("enter second number"))

if first>second:
    print("Greatest is",first)
else:
    print("greatest is",second)    

    


   