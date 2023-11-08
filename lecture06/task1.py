def Parabola(x)->float:
    return x**2

def Line(x)->float:
    return 2*x

def Polinom(x)->float:
    return 2*x**4 - 3*x**3 + 67*x**2 - 6*x + 9

def IntervalInput():
    Test1 = False
    while Test1 == False:
        try:
            lower_boundary = int(input("Enter the lower boundary of your interval: "))
            Test1 = True
            Test2 = False
            while Test2 == False:
                try:
                    upper_boundary = int(input("Enter the upper boundary of your interval: "))
                    range(lower_boundary,upper_boundary+1).index(upper_boundary)
                    Test2 = True
                except ValueError:
                    print('Your upper boundary is not a number or less than lower boundary. Try again.')
            Test3 = False
            while Test3 == False:
                try:
                    accuracy = int(input("Enter the accuracy: "))
                    Test3 = True
                except ValueError:
                    print('Your accuracy value is not a number. Try again.')
        except ValueError:
            print('Your lower boundary is not a number. Try again.')
            
def GoldenSection(function, lower_boundary, upper_boundary, accuracy,type='min'):
    ext = None
    if type == 'min':
        QMin = False
        while QMin == False:
            x1 = upper_boundary - ((upper_boundary - lower_boundary) / 1.618)
            x2 = lower_boundary + ((upper_boundary - lower_boundary) / 1.618)
            y1 = function(x1)
            y2 = function(x2)
            
            if y1 >= y2:
                lower_boundary = x1
            else:
                upper_boundary = x2
                
            if abs(upper_boundary - lower_boundary) < accuracy:
                ext = round((upper_boundary + lower_boundary) / 2, 3)
                QMin = True
    if type == 'max':        
        QMax = False
        while QMax == False:
            x1 = upper_boundary - ((upper_boundary - lower_boundary) / 1.618)
            x2 = lower_boundary + ((upper_boundary - lower_boundary) / 1.618)
            y1 = function(x1)
            y2 = function(x2)
            
            if y1 <= y2:
                lower_boundary = x1
            else:
                upper_boundary = x2
                
            if abs(upper_boundary - lower_boundary) < accuracy:
                ext = round((upper_boundary + lower_boundary) / 2, 3)
                QMax = True
    
    return ext

import math
print(GoldenSection(math.sin,-10,10,0.001,'max'))