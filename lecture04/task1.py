from random import randint

#input check
Test = False
while Test == False:
    try:
        length = int(input("Enter length of your list: "))
        range(0,length)[length-1]
        Test=True
    except ValueError:
        print('Your input value is not a number. Try again.')
    except IndexError:
            print('Length cannot be less than 1. Try again.')
            
#random numbers list print
print([randint(-10000,10000) for i in range(0,length)])

