orig_list = [] #stands for "original liust." List that stores user_input. In other words, a list with pseudo-duplicated elements
new_list = [] #list created to store unique values from org_list, whcih does not contain duplicated elements

while True: #While loop to make user initialize input until met with a condition
    null = '' #named variable as null which sotres an empty string hence NULL
    user_input = input("")

    if user_input == null: #if user input is _null then the while loop will break
        break
    else: #if !null:
        orig_list.append(user_input) #appends user_input to orig_list
        for item in orig_list: #for loop that iterates over orig_list and checks if item is already in the new_list
            if item not in new_list: #if item is not in new_list then then it appends item or user_input to new_list 
                new_list.append(item)
#once loop breaks, new_list is printed with separated values
print('\n', *new_list,sep='\n')