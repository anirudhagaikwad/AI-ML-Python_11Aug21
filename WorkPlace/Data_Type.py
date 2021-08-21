#integer
x = 10
y = 5
print(type(x))
# it will be the integer as long as the value is a whole number.
print(x)
print(x+y)
x=8
print(x+y)

#float
f=10.25
print(type(f))

#complex

a = 3.14J
print(type(a))



#boolean

num = 5 > 4
#num is the boolean variable
type(num)
#the output will be bool
print(num)
#this will print true.


#string

name = 'python'

name[2] 
#this will give you the output as 't'
name1='java'
result=name1.upper()
print(result)
result1=result.lower()
print(result1)



#list

list=['hi',10, 20,45]
print(list)
list.reverse()
print(list)
list[0:2]
print(list)
list.append(88)#append for what we pass they add in list at the end

print(list)
list.insert(2, 'hello')# insert is used for whatever we pass with index no. they add in that index no.
print(list)

value=list[0:2]
print(value)#only print 2 index value

list.clear()
print(list)#clearlist

#tuples
mytuples = (10,78,58,78,78)
print(mytuples)
res=mytuples.count(78)
print(res)

# ind=mytuples.index(78)
# print(ind)



#set

myset={10,45,89}
print(myset)#print all values

myset.add('java')
print(myset)#add java at the end

myset.remove(45)
print(myset)#remove 45


#Dictionary

mydictionary= {1: 'data science',2: 'python','third': 'machine learning' }
data=mydictionary[1]
print(data)#get data

mydictionary['fourth'] = 'structure'
print(mydictionary)# add new but incorrect name 

mydictionary['fourth'] = 'data structure'
print(mydictionary)# add new with correct name

mydictionary.pop('fourth')
print(mydictionary) #remove




