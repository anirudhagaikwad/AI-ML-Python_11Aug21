#simple

# i = 0
# while i<5:
#     print("the value of i is",i)
#     i +=1
# print("finished while loop") 


#infinite loop

# i = 0;
# while True:
#     i = i+1
#     print("hi",i)
#     break

#break

# x = 1
# while x <= 5:
#     print(x)
#     if x == 3:
#         break
#     x = x+1

#continue

# x = 1
# while x <= 5:
#     if x == 3:
#         x = x+1
#         continue
#     else:
#         print(x)
#         x = x+1

#neasted while loop
 
# i = 0
# j = 5
# while i<6:
#     while j>0:
#         print(i,j)
#         i= i+1
#         j= j-1        




# n = int(input("enter number"))
# sum = 0
# i = 1
# while i<=n:
#     sum = sum+i
#     i+=1
# print("the sum of first",n,"numbers is:",sum)  

#python=nohtyp
#reverse string

s = input("enter string")
output = ""
i = len(s)-1
while i>=0:
    output = output+s[i]
    i = i-1
print(output)    