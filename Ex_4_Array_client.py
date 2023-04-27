#Author: Edwin Gumba Jr.
#Description: A .py file that uses the methods found in Array.py. In our case, we're creating multiple arrays and finding the Max value within it.
#Date of submission: 4/27/23

import Ex_4_Array_main as Array #Imported Array_main as Array for easy access
maxSize = 10                    # Max size of the array
arr = Array.Array(maxSize)      # Create an array object

#IMPORTANT NOTE: THIS IS WHERE YOU EDIT ARRAY LIST 1, 2, AND 3. 
#You can edit the array list 1, 2, and 3 to create a new array.

#ARRAY 1
#array with various data types   
arr.insert(77)                  # Insert 10 items
arr.insert(99.8)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)

maxnum1 = arr.getMaxNum() #getter haha
print (maxnum1)

#ARRAY 2
arr2 = Array.Array(3) #Array with no values
maxnum2 = arr2.getMaxNum()
print (maxnum2)

#ARRAY 3
arr3 = Array.Array(5) #Array with words only
arr3.insert('Hello')
arr3.insert('I am')
arr3.insert('Edwin')
arr3.insert('Gumba')
arr3.insert('Jr')
maxnum3 = arr3.getMaxNum()
print (maxnum3)