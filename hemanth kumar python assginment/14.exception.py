
#1. Write a program to generate Arithmetic Exception without exception handling

try:
    a = 10/0
    print (a)
except ArithmeticError:
    print ("This statement is raising an arithmetic exception.")
else:
    print ("Success.")   
#-----------------------------------------------------------------------------

#6.Write a program to create your own exception

class notaccepted(Exception):
  def __init__(self, hai):
    self.hai=hai
 
try:
  raise notaccepted("i'm busy right now")
 
except notaccepted as err:
  # perform any action on YourException instance
  print("Message:", err.hai)


#-----------------------------------------------------------------------------
#7. Write a program with finally block


#Implementing try,except and finally

try:
    x=int(input("Enter First No:"))   
    y=int(input("Enter Second No:"))  
    z=x/y
    print(z)


except(ZeroDivisionError):
    print("2nd No cannot be zero") 

finally:    # here prints msg of finally block before terminating abnormally
    print("welcome to hyd...........")
   
print("end")
#Try the execution for all the 3 cases ,in all 3 cases finally will be executed


#-----------------------------------------------------------------------------
#9. Write a program to generate FileNotFoundException
    
#FileNotFoundError:
try:
    f=open("C:/data/demo5.txt","r")   #r--->read mode
    print(f.read())
    f.close()

except(FileNotFoundError):
    print("File doesnt exist")
    
except:
    print("Error")

else:
    print("File opened Successully")
print("end")


#------------------------------------------------------------------------------





















