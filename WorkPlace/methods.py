#instance methods

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print('hi',self.name)
        print('your marks are',self.marks)

    def grade(self):
        if self.marks>=75:
            print('you got First class')        
        elif self.marks>=60:
            print('you got second class')    
        elif self.marks>=35:
            print('you got third class')  

        else:
            print('you got failed')

n=int(input('enter number of students:'))

for i in range(n):
    name=input('enter name:')
    marks=int(input('enter marks:'))
    s=Student(name,marks)
    s.display()
    s.grade()


#syntax

def setvariable(self,variable):
    self.variable=variable  


# # eg.
def setName(self,name):
        self.name=name
            
#@@@

class Student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name  

    def setMarks(self,marks):
        self.marks=marks

    def getMarks(self):
        return self.marks 

n=int(input('enter number of students:'))

for i in range(n):
    s=Student()
    name=input('enter name:')
    s.setName(name)
    marks=int(input('enter marks:'))
    s.setMarks(marks)       
    print('hi',s.getName())
    print('your marks:',s.getMarks())


#class method

class Animal:
    legs=4
    @classmethod
    def Walk(cls,name):
        print('{} walks with {} legs'.format(name,cls.legs))
Animal.Walk('dog')
Animal.Walk('cat')

#static method

class Maths:

    @staticmethod
    def add(x,y):
        print('the sum:',x+y)

      
    @staticmethod
    def product(x,y):
        print('the product:',x*y) 

    @staticmethod
    def avg(x,y):
        print('the avg:',(x+y)/2)
Maths.add(10,20)
Maths.product(10,20)  
Maths.avg(10,20)  

#innerclass


class Outer:
    def __init__(self):
        print('outer class object creation')

    class Inner:
        def __init__(self):
            print('inner class object creation') 

        def m1(self):
            print('inner class method') 


Outer().Inner().m1() 

# Another ex.

class Person:
    def __init__(self):
        self.name='Tushar'
        self.dob=self.Dob()

    def display(self):
        print('name',self.name)
        self.dob.display()      

    class Dob:
        def __init__(self):
            self.dd=15
            self.mm=11
            self.yy=1947

        def display(self):
            print('dob={}/{}/{}'.format(self.dd,self.mm,self.yy))                     
p=Person()
p.display()