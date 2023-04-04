import math

def calculate_triangle():
    try:
        a = float(input("Input side A: "))
        b = float(input("Input side B: "))
        c = float(input("Input side C: "))

        if a <= 0 or b <= 0 or c <= 0:
            print("\n- Invalid input: Negative or Input is Equal to 0 -\n")
            return
        
        if (a+b<=c) or (b+c<=a) or (c+a<=b):
            print("\n- Invalid input: Triangle Inequality Theorem not Observed-\n")
            return
        
        if a == b == c:
            triangle_type = "Equilateral Triangle"

        elif a==b or b==c or a==c:
            triangle_type = "Isosceles Triangle"

        else:
            triangle_type = "Scalene Triangle"
        
        s = (a + b + c) / 2
        area = math.sqrt(s*((s-a)*(s-b)*(s-c)))
        print(f'\nIdentify the triangle_type: {area}')
        print(f'The triangle_type of triangle is: {triangle_type}\n')

    except ValueError:
        print("- Error: Invalid Input -\n")

while True:
    calculate_triangle()
    while True:
        choice = input("Do you wish to Continue? [Y/N]: ").lower()
        if choice == 'y':
            print("\n - Continue - \n")
            break
        elif choice == 'n':
            print("\n - Good Bye - \n")
            exit()
        else:
            print("\n - Invalid Input - \n")
            continue