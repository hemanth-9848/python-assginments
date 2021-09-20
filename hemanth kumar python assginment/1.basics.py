#1. Write a program to print your name
print("my name is hemanth kumar:")
#---------------------------------------------------------------------------

#2 Write a program for a Single line comment and multi-line comments

#giving values to the variables
x=10
y=20
#adding x and y
z=x+y
#printing the addition of both the variables
print("z=",z)

#-----------------------------------------------------------------------------
#3.Define variables for different Data Types int, Boolean, char, float, double
#   and print on the Console.

x=2
print(x,type(x))    #int
y=3.3
print(y,type(y))    #float
z=True
print(type(z))      #boolean

#-----------------------------------------------------------------------------

#4.Define the local and Global variables with the same name and print both
#  variables and understand the scope of the variable

x=10    #global variables
def display():
    x=10  #local variable
    print(x)
display()

#----------------------------------------------------------------------------


















