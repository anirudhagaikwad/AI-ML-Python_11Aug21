class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def talk(self):
        print("hello i am",self.name)
        print("my marks",self.marks)

s1=Student("Pankaj",80) 
s2=Student("Ashutosh",90)
s2.talk()


class Test:
    def __init__(self):
        print("constructor execution")

    def m1(self):
        print("methode execution")
t1=Test()
t2=Test() 
t3=Test()            





class Student:
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z

    def display(self):
        print("student name:{}\nrollno:{}\nmarks:{}".format(self.name,self.rollno,self.marks))

s1=Student("Pravin",100,85)  
s1.display()   

s2=Student("Anand",101,75)
s2.display()


#inside Constructor by using self variable

class Employee:
    def __init__(self):
        self.eno=100
        self.ename="Prasad"
        self.esal=50000

e=Employee()   
print(e.__dict__)    


#inside instance methode by using self variable 


class Test:
    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        self.c=30

t=Test()   
t.m1()
print(t.__dict__)


#outside of the class by using object ref. variable
class Test:
    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        self.c=30

t=Test()   
t.m1()
t.d=40
print(t.__dict__)












