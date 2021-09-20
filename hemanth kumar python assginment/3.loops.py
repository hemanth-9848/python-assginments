
#1.Write a program to print “Bright IT Career” ten times using for loop
x=[1,2,3,4,5,6,7,8,9,10]

for p in x:
    print("Bright IT Career")
    
#-----------------------------------------------------------------------------

#2. Write a python program to print 1 to 20 numbers using the while loop.

x=0
while(x<=9):
    x=x+1
    print(x)
print("end")
print("\n\n\n")
#----------------------------------------------------------------------------

#3. Program to equal operator and not equal operators

a=10
b=20
if(a==b):
    print("a is equal to b")
else:
    print("a is not equal to b")
x=25
y=25
if(x!=y):
    print("x is ot equal to y")
else:
    print("x is equal to y")
    print("\n\n\n")
    

#----------------------------------------------------------------------------

#4.write a program to print the odd and even numbers.

x=int(input("enter the value of x:"))
mod=x%2
if mod>0:
    print("x is the odd number")
else:
    print("this is even number")
print("\n\n\n")

#----------------------------------------------------------------------------
#5. Write a program to print largest number among three numbers.

x=int(input("Enter value of x:"))
y=int(input("Enter value of y:"))
z=int(input("Enter value of z:"))

if(x>y):
    if(x>z):
        print(x,"is the largest!!!")
    else:
        print(z,"is the largest!!!")
else:
    if(y>z):
        print(y,"is the largest!!!")
    else:
        print(z,"is the largest!!!")
print("end")
print("\n\n\n")
#----------------------------------------------------------------------------

#6. Write a program to print even number between 10 and 20 using while

n=10
while n<=20:
    print(n)
    n+=2
    
#---------------------------------------------------------------------------

#7. Write a program to print 1 to 10 using the do-while loop statement.
value=1
while True:
    print(value)
    value+=1
    if value>10:
        break

#---------------------------------------------------------------------------

#8. Write a program to find Armstrong number or not

x=int(input("enter the value of x:"))
sum=0
temp=x
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if x==sum:
    print(x,"is the armstrong number")
else:
    print(x,"is not an armstrong number")

#---------------------------------------------------------------------------

#9. Write a program to find the prime or not.
    
x=int(input("enter the value of x:"))
if x>1:
    for i in range(2,int(x/2)+1):
        if(x%i)==0:
            print(x,"is not a prime number")
            break
    else:
        print(x,"is a prime number")
else:
    print(x,"is not a prime number")

#----------------------------------------------------------------------------

#10. Write a program to palindrome or not.
    
x=int(input("Enter number:"))
temp=n
rev=0
while(x>0):
    dig=x%10
    rev=rev*10+dig
    x=x//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

#-----------------------------------------------------------------------------









