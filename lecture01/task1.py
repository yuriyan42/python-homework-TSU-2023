def law_of_cosines():
    from math import sqrt,cos,pi
    
    print("Enter a first side:")
    side1 = float(input())
    print("Enter a second side:")
    side2 = float(input())
    print("Enter an angle:") #value should be in degrees
    angle12 = float(input())*pi/180
    
    return sqrt(side1**2 + side2**2 - 2*side1*side2*cos(angle12))


print("The 3rd side is: ",law_of_cosines())
    