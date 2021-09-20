
#1. Write a class with a default constructor, one argument constructor and two argument 
#constructors. Instantiate the class to call all the constructors of that class from a main 
#class

class cube:
    def __init__(self):
        self.length=int(input("enter the length:"))
        self.breath=int(input("enter the breath:"))
        self.height=int(input("enter the height:"))
    def compute(self):
        self.volume=self.length*self.breath*self.height
        print("volume=",self.volume)
c1=cube()
print(c1)
c1.compute()
print("enter the values of the 2'nd cube:")
c2=cube()
print(c2)
c2.compute()
print("\n\n\n")

#------------------------------------------------------------------------------

#disadvantages of defualt contructor:
class student:
    def __init__(self):
        self.name="hemath"
        self.age=22
s1=student()

print(s1.name)  #default values
print(s1.age)
s1.name="ravi"    #modifying values
s1.age=18
print(s1.name)
print(s1.age)

s2=student()
print(s2.name)
print(s2.age)   #defualt values
s2.name="ajay"
s2.age=22
print(s2.name)
print(s2.age)

#here every time the constructor is initializing the nonstatic variable with
#same values,but i want different values for each object during object creation
#only,then go for parameterized constructor, which specifies different values
#for each object










      


















