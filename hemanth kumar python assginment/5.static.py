#1. Define a static variable and access that through a class
#ans
'''
   * a the variable defined with in the class and outside the method of a class
      are know as a static variable 
   *object to object data is common
   *for static variables memory is allocated only once
'''
class sample:
  x=10  #static variable
  y=20  #static variable
  def display(self):
      print(sample.x)     #accesing static variable
      print(sampe.y)
  def show(self):
      print(sample.x)
      print(sample.y)
#end of the class
print(sample.x)
print(sample.y)    #accesing sv from outside the class using class name

#-----------------------------------------------------------------------------

#2. Define a static variable and access that through a instance














