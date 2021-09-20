#1.write a function for arithmetic operators(+,-,*,/)

x=10
y=30
z=x+y
print(z)
r=x-y
print(r)
f=x*y
print(f)
c=x/y
print(c)

#---------------------------------------------------------------------------
#2. Write a method for increment and decrement operators(++, --)
a=b=c=1
print(id(a))
print(id(b))
print(id(c))
#Above all have the same id
# Now increment a
a+=1
print(id(a))
print(id(b))
print(id(c))


#--------------------------------------------------------------------------

#3. Write a program to find the two numbers equal or not
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
if x==y:
    print("two numbers are equal")
else:
    print("two numbers are not equal")

#--------------------------------------------------------------------------
#4.Program for relational operators (<,<==, >, >==)
x=10
y=20
z=30

p=(x>y) and (y>x)
print(p)

q=(x>y) and (z==x+y) or (x!=z)
print(q)

r=(x>y) and (y==z-x) or (z>y)  
print(r)

print(not True)
print(not False)
#---------------------------------------------------------------------------
#5. Print the smaller and larger number

x=[10,20,30,40,50,60]
print("largest element of the list:",max(x))
print("smallest element of the list:",min(x))




















