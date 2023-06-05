#https://www.tutorialspoint.com/python-program-to-check-whether-a-string-is-a-palindrome-or-not-using-recursion

def isPalindrome(user_string):                                  #Function to check if palindrome or not
    if len(user_string) < 2:                                    #Base Case, and will return True using recursion.
        return True                                             #Return true if string has 0 or 1 character (based on Base Case) and is Palindrome (True)
    elif user_string[0] == user_string[-1]:                     #Check if first character ([0]) and last character ([-1]) are equal.
        return isPalindrome(user_string[1:-1])                  #Slices the list and applies recursion. passing this updated string as an argument to isPalindrome repeatdly
    else:
        return False                                            #Last characters ae different. String is NOT a palindrome
    

def main(): #Main Def
    check_palindrome = input("User Input for Palindrome: ")     #Main INput String
    choice = input("Case Sensitive? [y / n]: ")                 #string to see user choice

    #if statement to see if user wants to lowercase palindrome or not
    if choice.lower() == "y":                                   #if yes, convert string into lower so ex: Maam returns True
        user_string = check_palindrome.lower()
        print(isPalindrome(user_string))                        #print result of isPalindrome 
    elif choice.lower() == "n":                                 #if n, check_palindrome will  be case sensitive so ex: Maam returns False
        print(isPalindrome(check_palindrome))                   
    else:
        print("Invalid choice")                                 #choice invalid if yes

main() #Initialize Main

#Special Mention to Danziel Cempron forsugegsting "if len(user_string) < 2" instead of < 1
#The string cannot be a palindrome if its length is 0, which indicates that there are no characters remaining to compare