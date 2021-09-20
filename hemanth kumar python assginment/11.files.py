
#1. Write a program to read text file

file=open("E:/jala/hemanth.txt","r")
x=file.read()
print(x)
file.close()

#----------------------------------------------------------------------------


#----------------------------------------------------------------------------
#5. Write a program to read a file a just to a particular index using seek()



# Opening "hemanth.txt" text file
f = open("hemanth.txt", "r")

# Second parameter is by default 0
# sets Reference point to twentieth
# index position from the beginning
f.seek(20)

# prints current position
print(f.tell())

print(f.readline())
f.close()
