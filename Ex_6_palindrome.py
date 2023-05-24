class Stack:
    def __init__(self, max):                # Constructor
        self.__stackList = [None] * max     # The stack stored as a list
        self.__top = -1                     # No items initially
    
    def push(self, item):                   # Insert item at top of stack
        self.__top += 1                     # Advance the pointer
        self.__stackList[self.__top] = item # Store item

    def isFull(self):                   # Check if stack is full #i used this to check if i implemented copypasted code correctly
        return self.__top == len(self.__stackList) - 1
    
    def checkPalindrome(self):             # Check if stack is a palindrome
        start = 0                       # reperesnets the idnex of the first item in the stack
        end = self.__top                # End is classiied as top 

        while start < end:
            first_item = self.__stackList[start].lower() #Sstart item is converted to a lower case
            last_item = self.__stackList[end].lower() #end item in teh stacklist is converted to lwoercase

            if first_item != last_item: #characters at the corresponding positions in the stack are not the same.
                return False 
            
            start += 1 #move to the next position
            end -= 1 #move to the previous position 
        return True

    def __str__(self):                  # Convert stack to string
        ans = "["                        # Start with left bracket
        for i in range(self.__top + 1):  # Loop through current items
            if len(ans) > 1:              # Except next to left bracket,
                ans += ", "                # separate items with comma
            ans += str(self.__stackList[i]) # Add string form of item
        ans += "]"                       # Close with right bracket
        return ans

stack = Stack(100)

phrase = "A man, a plan, a canal, Panama."
for char in phrase: #for each character in phrase
    if char.isalpha(): #check IF characters in string is alphabetical only.
        stack.push(char) #push char into stack

print(stack.checkPalindrome()) #Output MUST BE TRUE

#References: https://www.javatpoint.com/palindrome-program-in-python
#https://www.sanfoundry.com/python-program-check-string-palindrome-using-stack/