
1.# Create a Dictionary with at least 5 key value pairs of the Student ID and Name

#1.1. Adding the values in dictionary

stud={"sid":101,"sname":"hemanth","group":"cse",1:"male"}
print(stud)
print(type(stud))
print(len(stud))
print(stud["sname"])


#-----------------------------------------------------------------------------

#1.2. Updating the values in dictionary
marks = {'Physics':67, 'Maths':87}
internal_marks = {'Practical':48}

marks.update(internal_marks)

print(marks)

#-----------------------------------------------------------------------------

#1.3. Accessing the value in dictionary

print(stud["sname"])

#-----------------------------------------------------------------------------

#1.4. Create a nested loop dictionary
details={"name":"Ajay","age":25,"height":6.2}
    
for p in details:
    print(p,type(p))

#printing values using for loop
for p in details:
    print(details[p])

#----------------------------------------------------------------------------

#1.6. Print the keys present in a particular dictionary
x={"a":20,"b":5,"a":10,"b":15,"a":3}
print(x,len(x))
print(x['a'])  #if we pass the key----->we get the value
print(x['b'])

#----------------------------------------------------------------------------

#1.7. Delete a value from a dictionary
x={"name":"amar","branch":"CSE","Rank":5}
print(x)
print(id(x))
print(x["name"])
print(x.get("name"))
x.pop("branch") #removing particular key
print(x)








