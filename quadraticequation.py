import math
while input("Do you want to solve a quadratic equation?(y/n): ")=='y':
    print("Enter values for a, b, and c for the equation ax^2+bx+c=0")
    a=int(input("a: "))
    b=int(input("b: "))
    c=int(input("c: "))
    if a==0:
        print("This is a linear function, x equals")
        x=(-c/b)
        print(x)
    else:
        d=(b*b)-(4*a*c))
        if d < 0:
            print("Imaginary")
        else:
            print("Your two x values are: ")
            x1=((-b)+math.sqrt(d)/(2*a)
            print(x1)
            x2=((-b)-math.sqrt(d)/(2*a)
            print(x2)
exit()
