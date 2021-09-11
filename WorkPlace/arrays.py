#simple array
from array import*
arr = array('i',[10,20,30])
print(arr)

#specific element
a = array ('d',[1.1,2.1,5.8])
print(a[2])

#append()

arr = array ('i',[80,90,99])
arr.append(101)
print(arr)

#extend()

a = array('d',[8.9,7.5,4.5,1.2])
a.extend([3.1,3.2,3.3,3.4])
print(a)


a = array('i',[5,9,7,8])
b = array('i',[10,20,30])
c=a+b
print("array=",c)



#pop()
b = array('d',[9.8,9.7,9.4,5.6,1.1])
print(b.pop(3))

#remove()
a = array('i',[100,200,300,400])
a.remove(300)
print(a)

#slicing
arr = array('d',[10.1,20.1,30.1,40.1,50.1])
print(arr[0:4])





