
#1. Write a function to add integer values of an array
x=[10,20,30,40,50]
x.append(80)
#here append means adding a number to a list
print(x)

#----------------------------------------------------------------------------

#2. Write a function to calculate the average value of an array of integer

def Average(x):
	return sum(x) / len(x)

x=[20,40,50,60,70,80]
average = Average(x)

# Printing average of the list
print("Average of the list =", round(average, 2))

#-----------------------------------------------------------------------------
#3. Write a program to find the index of an array element
list1 = [1,2,3,4,1,1,1,4,5]
  
# Will print the index of '4' in list1
print(list1.index(4))
  
list2 = ['cat','bat','mat','cat','pet']
  
# Will print the index of 'cat' in list2 
print(list2.index('cat'))

#----------------------------------------------------------------------------
#4. Write a function to test if array contains a specific value
x= [1, 2, 3]
exists=2 in x  #it removes the value 2 from the list
print(exists)

#-----------------------------------------------------------------------------
#5. Write a function to remove a specific element from an array
x=[10,20,30,40,50]
del x[0]    #it remove the first value of the list and print all the elements
print(x)    #of the list

#-----------------------------------------------------------------------------

#6. Write a function to copy an array to another array
   
arr1=[1,2,3,4,5]    
     
#Create another array arr2 with size of arr1    
arr2=[None]*len(arr1)    
     
#Copying all elements of one array into another    
for i in range(0, len(arr1)):    
    arr2[i] = arr1[i]   
     
#Displaying elements of array arr1     
print("Elements of original array: ")   
for i in range(0, len(arr1)):    
   print(arr1[i])   
     
print()    
     
#Displaying elements of array arr2     
print("Elements of new array: ")   
for i in range(0, len(arr2)):    
   print(arr2[i])

#-----------------------------------------------------------------------------

#7. Write a function to insert an element at a specific position in the array

list1=[1,2,3,4,5,6,7]

# insert 10 at 4th index
list1.insert(4,10)
print(list1)

list2 = ['a','b','c','d','e']

# insert z at the front of the list
list2.insert(0,'z')
print(list2)

#-----------------------------------------------------------------------------

#8. Write a function to find the minimum and maximum value of an array

x=[1,2,3,4,5,6,7]
print("max:",max(x))
print("min:",min(x))

#-----------------------------------------------------------------------------

#9. Write a function to reverse an array of integer values
#Initialize array     
x=[1,2,3,4,5]    
print("Original array: ")    
for i in range(0, len(x)):    
    print(x[i])   
print("Array in reverse order: ")   
#Loop through the array in reverse order    
for i in range(len(x)-1, -1, -1):     
    print(x[i])     
#-----------------------------------------------------------------------------

#10. Write a function to find the duplicate values of an array
    
x=[1,2,3,4,2,7,8,8,3]     
     
print("Duplicate elements in given array: ")    
#Searches for duplicate element    
for i in range(0,len(x)):    
    for j in range(i+1,len(x)):    
        if(x[i] == x[j]):
            print(x[j])   
#-----------------------------------------------------------------------------

#11. Write a program to find the common values between two arrays

import numpy as np
x= np.array([0,1,2,3,4])
y=[1,3,4]

# Common values between two arrays
print(np.intersect1d(x,y))

#-----------------------------------------------------------------------------

#12. Write a method to remove duplicate elements from an array

def removeDuplicates(arr,n):

	# Return, if array is
	# empty or contains
	# a single element
	if n==0 or n==1:
		return n

	temp=list(range(n))

	# Start traversing elements
	j=0;
	for i in range(0,n-1):

		# If current element is
		# not equal to next
		# element then store that
		# current element
		if arr[i]!= arr[i+1]:
			temp[j]=arr[i]
			j += 1

	# Store the last element
	# as whether it is unique
	# or repeated, it hasn't
	# stored previously
	temp[j]=arr[n-1]
	j+=1
	
	# Modify original array
	for i in range(0,j):
		arr[i]=temp[i]

	return j

# Driver code
arr=[1,2,2,3,4,4,4,5,5]
n=len(arr)

# removeDuplicates() returns
# new size of array.
n=removeDuplicates(arr,n)

# Print updated array
for i in range(n):
	print ("%d"%(arr[i]), end = " ")

#-----------------------------------------------------------------------------
#13. Write a method to find the second largest number in an array
	
list1 = [10,20,4,45,99]

mx=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n =len(list1)
for i in range(2,n):
	if list1[i]>mx:
		secondmax=mx
		mx=list1[i]
	elif list1[i]>secondmax and \
		mx != list1[i]:
		secondmax=list1[i]

print("Second highest number is : ",\
	str(secondmax))
#-----------------------------------------------------------------------------
#15. Write a method to find number of even number and odd numbers in an array


def CountingEvenOdd(arr, arr_size):
	even_count=0
	odd_count=0
	
	for i in range(arr_size):

		if (arr[i]&1== 1):
			odd_count+=1
		else:
			even_count+=1

	print("Number of even elements = ",
		even_count)
	print("Number of odd elements = ",
		odd_count)

arr = [2,3,4,5,6]
n = len(arr)

# Function Call
CountingEvenOdd(arr,n)

#-----------------------------------------------------------------------------




































