# Implement an Array data structure as a simplified type of list. 

class Array(object):
   def __init__(self, initialSize):    # Constructor
      self.__a = [None] * initialSize  # The array stored as a list
      self.__nItems = 0                # No items in array initially

   def __len__(self):                  # Special def for len() func
      return self.__nItems             # Return number of items
   
   def get(self, n):                   # Return the value at index n
      if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
         return self.__a[n]            # only return item if in bounds
   
   def set(self, n, value):            # Set the value at index n
      if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
         self.__a[n] = value           # only set item if in bounds
      
   def insert(self, item):             # Insert item at end
      self.__a[self.__nItems] = item   # Item goes at current end
      self.__nItems += 1               # Increment number of items

   def find(self, item):               # Find index for item
      for j in range(self.__nItems):   # Among current items
         if self.__a[j] == item:       # If found,
            return j                   # then return index to item
      return -1                        # Not found -> return -1
   
   def search(self, item):             # Search for item
      return self.get(self.find(item)) # and return item if found

   def delete(self, item):             # Delete first occurrence
      for j in range(self.__nItems):   # of an item
         if self.__a[j] == item:       # Found item
            self.__nItems -= 1         # One fewer at end
            for k in range(j, self.__nItems):  # Move items from
               self.__a[k] = self.__a[k+1]     # right over 1
            return True                # Return success flag
      
      return False     # Made it here, so couldn't find the item   

   def traverse(self, function=print): # Traverse all items
      for j in range(self.__nItems):   # and apply a function
         function(self.__a[j])


   #Author: Edwin Gumba Jr.
   #Description: A function that finds the biggest number in an array 
   #Date of submission: 4/27/23

   #we're hardcoding the Max() function ahahaha
   #https://stackoverflow.com/questions/38622287/creating-a-max-function-from-scratch-python. Used 'index' to check for the index since using 'item' puts the list index out of range
   #I thank Mon Olarte for guiding me what to insert inside the array to get the expected output. 

   def getMaxNum(self): #accepts the argument (self) and accepts variables in a class
      highnum = None #Python uses the keyword None to define null objects and variables. If I won't use highnum then it ahs already been equated to NONE
      for index in range (self.__nItems): #This line initiates a loop that iterates through all of the array's indices. The range function returns 0 to self.__nItems
         if isinstance(self.__a[index], (float, int)): #if an element in the array's index contains the following data type: int and float, return TRUE. OMG THIS FUNCTION IS SO COOL
            if highnum == None or self.__a[index] > highnum: #This line checks if highnum is None or if the item at the current index is greater than highnum. If either is true, 'highnum' is updated in the current index
               highnum = self.__a[index] #Highnum is updated to reflect the item's current index.

      if highnum is None: #if statement to check if highnum is still none
         print("Array has no numbers, therefore: ")
         return None
      else:
         print("Maximum number in array is: ")
         return highnum #At the end of the loop, this line returns the value of highnum, which should be the highest integer found in the array. If no numbers are discovered in the array, highnum will remain None.