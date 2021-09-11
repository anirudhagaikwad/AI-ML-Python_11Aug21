class A:
    def feature1(self):
        print("feature 1 working")

    def featur2(self):
        print("feature 2 working")

class B(A):
    def feature3(self):
        print("feature 3 working")

    def featur4(self):
        print("feature 4 working")

b1=B()
b1.featur2()   


#multilevel

class A:
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B(A):
    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")

class C(B) :
    def feature5(self):
        print("feature 5 working")

c1=C()  
c1.feature2()
c1.feature3()
c1.feature5()

#multiple


class A:
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B:
    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")

class C(A,B) :
    def feature5(self):
        print("feature 5 working")


c1=C()
c1.feature1()
c1.feature3()

#@@
class A:
    def __init__(self):
        print('in a init')

    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B(A):
    def __init__(self):
        super().__init__()
        print('in b init')

    def feature3(self):
        print("feature 3 working")


b1=B()
