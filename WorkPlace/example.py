#odd &  even
num = int(input("enter a number"))
if (num % 2)==0:
    print("is even")  
else:
    print("is odd")


#age cal

first  = int(input("enter first number"))
second = int(input("enter second number")) 
third = int(input("enter third number"))

if first > second and first > third:
    print("oldest is", first)
elif second > first and second > third:
    print("oldest is",second)
elif third > first and third > second:
    print("oldest is",third)

if first <=second and first < third:
    print("youngest is",first) 
elif second < first and second <third:
    print("youngest is",second) 
elif third < first and third < second:
    print("youngest is",third)
else:
    print("all are equal") 

#cal area

side = [5,4,7,8,9,3,8,2,6,4] 

for y in side:
    print("square of", y,"is")
    y=y*y
    print(y)

