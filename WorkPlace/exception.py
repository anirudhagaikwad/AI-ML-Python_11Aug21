#simple
x = int(input('enter a number'))
y = int(input('enter a number'))
print(x/y)


#exception
x = int(input('enter a number'))
y = int(input('enter a number'))
try:
    print(x/y)

except Exception:
    print("you cannot divide by zero")   

#@@@
a = int(input("enter a no."))
b = int(input("enter a no."))

try:
    print("open resource")
    print(a/b)
    

except Exception as e:
    print("you cannot divide by zero",e)
    

finally: 
    print("close resource")  

  
#@@@

try:
    x = int(input("enter a no."))
    y = int(input("enter a no."))
    print(x/y)

except Exception as e:
    print("something went wrong",e)


finally:
    print("successfully executed")

