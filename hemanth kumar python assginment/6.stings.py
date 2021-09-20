
#1. Different ways creating a string
#ans

#In Python,A String is represented using
'''
1.single quote(' ')
2.Double quote(" ")
3,Triple quote('''   ''')

Each character of a string is accessed or identified by using a unique index

String supports 2 types of indexes:
    1.Forward index(or) Positive index-------->starts from left to right ---->starts with 0
    2.Backward index(or) Negative index ------>starts from right to left----->starts with -1
'''

#------------------------------------------------------------------------------------

#2. Concatenating two strings using + operator
x="python"

print(x)
print(type(x))
print(id(x))
print(len(x))
y="programming"
print(x+" "+y) #Concatenation--->adding 2 strings-->1st string follwed by 2nd sting

#------------------------------------------------------------------------------

#3. Finding the length of the string
x="hemanth"
print(len(x))

#-----------------------------------------------------------------------------

#4. Extract a string using Substring


#Extracting particular portion of a string
x="python program"

print(x)

#extract----->"python"
print(x[0:6]) #always upper bound is excluded

#Extract---->"prog"
print(x[7:11])

#-----------------------------------------------------------------------------

#5. Searching in strings using index()


x="python program"
#Extract----->"program"
print(x[7:14])
print(x[7: ])
print(x[-7: ])

#--------------------------------------------------------------------------
#6. Matching a String Against a Regular Expression With matches()

#---------------------------------------------------------------------------
#7.Comparing strings

#comparision stings in python areThe relational operators compare the Unicode
#values of the characters of the strings from the zeroth index till the end of
#the string. It then returns a boolean value according to the operator used.


#---------------------------------------------------------------------------

#8. startsWith(), endsWith() and compareTo()
#startswith()
#endswith()

x="python is easier than Java"
print(x.startswith("python"))
print(x.endswith("Java"))


#--------------------------------------------------------------------------

#9. Trimming strings with strip()

#strip(): for removing the blankspaces before and after the string
x="          Good Morning Hyderabad           "
print(x,len(x))
y=x.strip()
print(y,len(y))

#--------------------------------------------------------------------------
#10. Replacing characters in strings with replace()
#replace(): for replacing a portion of a string

x="Java is Easy and Java is simple"
print(x)
print(x.replace("Java","Python"))


#-------------------------------------------------------------------------
#11. Splitting strings with split()
#split(): If we split a string,we get a list

x="Good Morning Hyderabad"
y=x.split(" ")
print(y,type(y))
print(y[2])
#-------------------------------------------------------------------------
#12. Converting integer objects to Strings

#----------------------------------------------------------------------------
#13. Converting to uppercase and lowercase

#1.upper(): For converting a string to uppercase
x="hyderabad"
print(x.upper())

#2.lower(): for converting a string to lowercase
x="CHENNAI"
print(x.lower())








































