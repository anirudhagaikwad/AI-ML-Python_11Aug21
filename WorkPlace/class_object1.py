#how to access instance variable

class Test:
    def __init__(self):
        self.a=10
        self.b=20

    def display(self):
        print(self.a)
        print(self.b)

t=Test()
t.display()
print(t.a,t.b)  

#how to del instance variable

class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40

    def m1(self):
        del self.d

t=Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
del t.c
print(t.__dict__)


#static

class Test:
    x=10

    def __init__(self):
        self.y=30

t1=Test()
t2=Test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
Test.x=888
t1.y=999
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)


#how to access static variable

class Test:
    x=10
    def __init__(self):
        print(self.x)
        print(Test.x)

    def a1(self):
        print(self.x)
        print(Test.x)
t=Test()
print(Test.x)
print(t.x)



