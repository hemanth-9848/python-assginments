
#1. Create a class with PRIVATE fields, private method and a main method.
#   Print the fields in main method. Call the private method in main method.

class sample:
    hname=input("ENTER THE HUSBAND NAME:")
    wname=input("ENETR THE WIFE NAME:")
    hage=float(input("ENTER THE HAGE:"))
    __wage=float(input("ENTER THE WAGE:"))
    __sal=float(input("ENTER THE SALARY:"))
s1=sample()
print("hname:",sample.hname)
print("wname:",sample.wname)
print("Husband Age:",sample.hage)
#print("Wife Age:",sample.__wage)
#print("salary:",sample.__sal)

class B:
    print("husband age=",sample.hage)
    #print("salary:",sample.__sal)
    print("\n\n\n")
#-----------------------------------------------------------------------------
'''
2.  Create a class with PUBLIC fields and methods. 
Access the public methods and fields from any class in the same package or
different package
'''

p=70   #global variable
def show():
    print("hello")   #fuction this function can be accesed by all the class and
                     #methods
class A:
    x=10
    print(x)
    def __init__(self):
        self.y=20
        print("constructor of A")
    def display(self):
        print("Hello from class A")
        print("p=",p)  #global variable
        show()
class B(A):   #class B is extending class A
    z=30
    print(z)
    def display2(self):
        print("hello from class B")
    def show(self):
        global p     #forward declaration
        print("x=",self.x)  #accesing x of class a,sv accessd using class name
        print("y=",self.y)  #accesing y of class b,nsv accessd using self
        print("z=",B.z)
        p=75
        sum1=B.x+self.y+B.z  #sum1 is the local variable
        print("sum:",sum1)
        print("p=",p)
        self.display()
        self.display2()
        show()
b1=B()
b1.show()
print(B.x)
print(b1.y)
#print(sum1) local variables can't be accesed
print(p)




    
