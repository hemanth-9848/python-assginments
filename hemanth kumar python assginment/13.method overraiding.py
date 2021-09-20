'''
class test:
    def __init__(self):
        self.a=10
        self.b=20
        print("a=",self.a)
        print("b=",self.b)
    def __init__(self,p,q):
        self.x=p
        self.y=q
    def display(self):
        print("a=",self.a)
        print("b=",self.b)
        print("x=",self.x)
        print("y=",self.y)
#end of the class
t1=test(9,10)
t1.display()
t2=test(12,30)
t2.display()
#error because of the method overloading
'''
#-----------------------------------------------------------------------------

def sum(a,b):
    x=a*b
    print(x)
def sum(a,b,c):
    x=a*b*c
    print(x)
sum(4,5,5)

# in the above code, we have defined two sum method, but we can only use the
#secound product method,as python does not support method of the same name and
#different arguments, but we can only use the latest defined method,calling
#the other method will produce an error,like calling product(4,5) will produce
#an error as the latest defined sum method takes three arguments thus overcome
#the above problem we can use different ways to achive the method

#-----------------------------------------------------------------------------

#1. Write two methods with the same name but different number of parameters
#of same type and call the methods

class sample:
    x=10
    y=20
    def m1(self):
        self.a=40
        self.b=50
        print("a=",self.a)
        print("b=",self.b)
    def m1(self):
        self.f=20
        self.z=40
        print("f=",self.f)
        print("z=",self.z)
s1=sample()
print(sample.x)
print(sample.y)
s1.m1()
s1.m1()

#always the latest method will be executed

#-----------------------------------------------------------------------------






