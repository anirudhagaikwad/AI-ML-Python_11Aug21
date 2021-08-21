#addition

a=10
b=2
# c=a+b
a+=b
print(a)

#sub
a=10
b=2
a-=b

print(a)

#sub
a=8
b=4
a=a-b
print(a)


#multiplicatin
x=5
y=5
x*=y
print(x)

#division
a=8
b=2
a/=b
print(a)

#modulus

a=5
b=10
a%=b
print(a)

#floor divide
a=5
b=8
a//=b
print(a)

#exponent
a=2
b=3
a**=b
print(a)

#logical

#AND
a=10
b=-10
c=0

result=a>b and b>c
print('result', result)

result1=a<b and b<c
print('result1',result1)



result2=a>b and c>b
print('result2',result2)


a=10
b=-10
c=0
result_1=a>b or b>c
print('result_1',result_1)

result_2=a>b or b<c
print('result_2',result_2)

result_3=a<b or c<b
print('result_3',result_3)


#not
x="true"
print(not x)

y="5"
d=not y
print( not d)

#add
a=10
b=10
c=0
d=5

reslt_add= a>b and b<c and d>c
print('result_add', reslt_add)



