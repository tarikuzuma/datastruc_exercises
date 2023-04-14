#Special thanks to: https://www.youtube.com/watch?v=eUiIZfAtBCI  for the logic of GCDs which i forgot in college haha
#Function that has m and n as parameters. Function that also finds the GCD
def getGcd(m, n):
    #If condition to find smallest number between n and m
    #d is essentially the variable for smallest number
    if m > n:   #if m is greater than n then make n = d
        d = n 
    else:
        d = m   #if n is greater than m then equal m to d

    #Essentially a while loop that finds the Common Divisor of both n and m
    #To check if the Modulo of m and d and vice versa is not even. 
    while m % d != 0 or n % d != 0: 
        d -= 1 #Decreases d by 1 and continues to find the GCD of m and n
    return d

#Call on the main function
def main():
    # Enter your code here. Read input from STDIN. Print output to STDOUT

    #m and n asks user to input positive integers (already assumes)
    m = int(input("Input First Positive Integer Here: "))
    n = int(input("Input Second Positive Integer Here: "))

    #variable `greatest_common` is assigned when finding the GCD, accepts both m and n as parameters
    greatest_common = getGcd(m,n)

    #prints GCD of both n and m
    print ("Their greatest Common Divisor is: ", greatest_common)

main()