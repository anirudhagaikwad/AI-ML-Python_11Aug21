#call function

def my_function():
    print("hello")

my_function()


#argument Function

def function(fname):
    print(fname + "ref")

function("email")
function("phone")


#number of arguments

def noarg(fname,lname):
    print(fname + ""+lname)

noarg("amar","Joshi")

#arbitrary arguments

def my_funcion(*kids):
    print("the Youngest child is"+kids[1])

my_funcion("Avinash","Pankaj","Pramod")


#keyword arguments

def key_arg(child3,child2,child1):
    print("the Youngest child is"+child3)

key_arg(child1="Ashutosh",child2="Rohit",child3="Anand")


##**
def fun_star(**kid):
    print("His last name is"+kid["lname"])
    print(type(kid))
# fun_star(fname="raj",lname="Patil")
fun_star(lname="Jadhav")


#default 

def default_par(country = "norway"):
    print("i am from"+country)

default_par("Brazil")
default_par()


#list arguments

def list_arg(fruits):
    for x in fruits:
        print(x)

fruits = ["apple","cherry"]

list_arg(fruits)

Pass statement

def pass_fun():
    pass

#@@@@
def sum(numbers):
    total =0
    for s in numbers:
        total+=s
    return total

print(sum((8,2,3,0,7,5)))


#1)(8,5,6)
#2)4321abcd
#dcba1234




