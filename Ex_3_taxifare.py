def getFare(time, distance): #Function that uses time and distance as parameters
    return 40 + (time * 2) + (distance * 13.5)

def main(): #main function
    while True: #try-catch to see if user inputs int
        try:
            time = int(input("Input how long it took to travel (minutes): ")) #variable to see user time in minutes
            distance = int(input("Insert distance travelled (km): ")) #variable to see user distance in km
            print("\nTotal fare is: Php", getFare(time, distance)) #prints function getFare with necessary parameters
        except:
            print ("\n- Numerical digits only -") 

main ()