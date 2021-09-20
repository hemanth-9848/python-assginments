
#1. Create a program to create two class.

class student:
    def __init__(self,name,age):   #parameterized
        self.stname=name
        self.stdage=age
    def display(self):
        print("name:",self.stname)
        print("age:",self.stdage)
s1=student("hemanth",24)
s1.display()
s2=student("miller",28)
s2.display()
s3=student("ravi",22)
s3.display()
