class A:
    a=10
    b=20     #static variable
    def m1(self):
        print("from super class:")
        self.x=4.5    #non static variable
        print("a=",A.a,id(A.a))
        print("x=",self.x)
class B(A):
    c=30
    d=40
    a=50
    def m2(self):
        print("from derived class:")
        B.a=B.a+5
        print("a=",B.a,id(B.a))
        print("b=",B.b)   #accesing b from class A
        print("c=",B.c)
        print("d=",B.d)
        print("a=",A.a)
        self.e=B.a+B.b+B.c+B.d    #creating a non static variable e
        print("e=",self.e)
        print("\n\n\n")
        self.m1()   #accesing method m1 of class A
        print("x=",self.x)
b1=B()
b1.m2()
b1.m1()
print(B.a)

        


        



        
