#hard enough without functions, loops and modules

TensList=["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
NumbersList=["one","two","three","four","five","six","seven","eight","nine"]
TeensList=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

number = input("Enter a number in range: (0, 99): ")

if len(number)<=2:
    if number[0] == "1":
        if len(number) == 2:
            if number[1] == "0":
                print(TeensList[0])
            elif number[1] == "1":
                print(TeensList[1])
            elif number[1] == "2":
                print(TeensList[2])
            elif number[1] == "3":
                print(TeensList[3])
            elif number[1] == "4":
                print(TeensList[4])
            elif number[1] == "5":
                print(TeensList[5])
            elif number[1] == "6":
                print(TeensList[6])
            elif number[1] == "7":
                print(TeensList[7])
            elif number[1] == "8":
                print(TeensList[8])
            elif number[1] == "9":
                print(TeensList[9])
            else:
                print("It is not a number!")
        elif len(number) == 1:
            print(NumbersList[0])   
    elif number[0] == "2":
        if len(number) == 2:
            if number[1] == "0":
                print(TensList[0])
            elif number[1] == "1":
                print(TensList[0]+NumbersList[0])
            elif number[1] == "2":
                print(TensList[0]+NumbersList[1])
            elif number[1] == "3":
                print(TensList[0]+NumbersList[2])
            elif number[1] == "4":
                print(TensList[0]+NumbersList[3])
            elif number[1] == "5":
                print(TensList[0]+NumbersList[4])
            elif number[1] == "6":
                print(TensList[0]+NumbersList[5])
            elif number[1] == "7":
                print(TensList[0]+NumbersList[6])
            elif number[1] == "8":
                print(TensList[0]+NumbersList[7])
            elif number[1] == "9":
                print(TensList[0]+NumbersList[8])
            else:
                print("It is not a number!")
        elif len(number) == 1:
            print(NumbersList[1])
    elif number[0] == "3":
        if len(number) == 2:
            if number[1] == "0":
                print(TensList[1])
            elif number[1] == "1":
                print(TensList[1]+NumbersList[0])
            elif number[1] == "2":
                print(TensList[1]+NumbersList[1])
            elif number[1] == "3":
                print(TensList[1]+NumbersList[2])
            elif number[1] == "4":
                print(TensList[1]+NumbersList[3])
            elif number[1] == "5":
                print(TensList[1]+NumbersList[4])
            elif number[1] == "6":
                print(TensList[1]+NumbersList[5])
            elif number[1] == "7":
                print(TensList[1]+NumbersList[6])
            elif number[1] == "8":
                print(TensList[1]+NumbersList[7])
            elif number[1] == "9":
                print(TensList[1]+NumbersList[8])
            else:
                print("It is not a number!")
        elif len(number) == 1:
            print(NumbersList[2])
    elif number[0] == "4":
        if len(number) == 2:
            if number[1] == "0":
                print(TensList[2])
            elif number[1] == "1":
                print(TensList[2]+NumbersList[0])
            elif number[1] == "2":
                print(TensList[2]+NumbersList[1])
            elif number[1] == "3":
                print(TensList[2]+NumbersList[2])
            elif number[1] == "4":
                print(TensList[2]+NumbersList[3])
            elif number[1] == "5":
                print(TensList[2]+NumbersList[4])
            elif number[1] == "6":
                print(TensList[2]+NumbersList[5])
            elif number[1] == "7":
                print(TensList[2]+NumbersList[6])
            elif number[1] == "8":
                print(TensList[2]+NumbersList[7])
            elif number[1] == "9":
                print(TensList[2]+NumbersList[8])
            else:
                print("It is not a number!")
        elif len(number) == 1:
            print(NumbersList[3])
    elif number[0] == "5":
        if len(number) == 2:
            if number[1] == "0":
                print(TensList[3])
            elif number[1] == "1":
                print(TensList[3]+NumbersList[0])
            elif number[1] == "2":
                print(TensList[3]+NumbersList[1])
            elif number[1] == "3":
                print(TensList[3]+NumbersList[2])
            elif number[1] == "4":
                print(TensList[3]+NumbersList[3])
            elif number[1] == "5":
                print(TensList[3]+NumbersList[4])
            elif number[1] == "6":
                print(TensList[3]+NumbersList[5])
            elif number[1] == "7":
                print(TensList[3]+NumbersList[6])
            elif number[1] == "8":
                print(TensList[3]+NumbersList[7])
            elif number[1] == "9":
                print(TensList[3]+NumbersList[8])
            else:
                print("It is not a number!")
        elif len(number) == 1:
            print(NumbersList[4])
    elif number[0] == "6":
        if len(number) == 2:
            if number[1] == "0":
                print(TensList[4])
            elif number[1] == "1":
                print(TensList[4]+NumbersList[0])
            elif number[1] == "2":
                print(TensList[4]+NumbersList[1])
            elif number[1] == "3":
                print(TensList[4]+NumbersList[2])
            elif number[1] == "4":
                print(TensList[4]+NumbersList[3])
            elif number[1] == "5":
                print(TensList[4]+NumbersList[4])
            elif number[1] == "6":
                print(TensList[4]+NumbersList[5])
            elif number[1] == "7":
                print(TensList[4]+NumbersList[6])
            elif number[1] == "8":
                print(TensList[4]+NumbersList[7])
            elif number[1] == "9":
                print(TensList[4]+NumbersList[8])
            else:
                print("It is not a number!")
        elif len(number) == 1:
            print(NumbersList[5])
    elif number[0] == "7":
        if len(number) == 2:
            if number[1] == "0":
                print(TensList[5])
            elif number[1] == "1":
                print(TensList[5]+NumbersList[0])
            elif number[1] == "2":
                print(TensList[5]+NumbersList[1])
            elif number[1] == "3":
                print(TensList[5]+NumbersList[2])
            elif number[1] == "4":
                print(TensList[5]+NumbersList[3])
            elif number[1] == "5":
                print(TensList[5]+NumbersList[4])
            elif number[1] == "6":
                print(TensList[5]+NumbersList[5])
            elif number[1] == "7":
                print(TensList[5]+NumbersList[6])
            elif number[1] == "8":
                print(TensList[5]+NumbersList[7])
            elif number[1] == "9":
                print(TensList[5]+NumbersList[8])
            else:
                print("It is not a number!")
        elif len(number) == 1:
            print(NumbersList[6])
    elif number[0] == "8":
        if len(number) == 2:
            if number[1] == "0":
                print(TensList[6])
            elif number[1] == "1":
                print(TensList[6]+NumbersList[0])
            elif number[1] == "2":
                print(TensList[6]+NumbersList[1])
            elif number[1] == "3":
                print(TensList[6]+NumbersList[2])
            elif number[1] == "4":
                print(TensList[6]+NumbersList[3])
            elif number[1] == "5":
                print(TensList[6]+NumbersList[4])
            elif number[1] == "6":
                print(TensList[6]+NumbersList[5])
            elif number[1] == "7":
                print(TensList[6]+NumbersList[6])
            elif number[1] == "8":
                print(TensList[6]+NumbersList[7])
            elif number[1] == "9":
                print(TensList[6]+NumbersList[8])
            else:
                print("It is not a number!")
        elif len(number) == 1:
            print(NumbersList[7])
    elif number[0] == "9":
        if len(number) == 2:
            if number[1] == "0":
                print(TensList[0])
            elif number[1] == "1":
                print(TensList[7]+NumbersList[0])
            elif number[1] == "2":
                print(TensList[7]+NumbersList[1])
            elif number[1] == "3":
                print(TensList[7]+NumbersList[2])
            elif number[1] == "4":
                print(TensList[7]+NumbersList[3])
            elif number[1] == "5":
                print(TensList[7]+NumbersList[4])
            elif number[1] == "6":
                print(TensList[7]+NumbersList[5])
            elif number[1] == "7":
                print(TensList[7]+NumbersList[6])
            elif number[1] == "8":
                print(TensList[7]+NumbersList[7])
            elif number[1] == "9":
                print(TensList[7]+NumbersList[8])
            else:
                print("It is not a number!")
        elif len(number) == 1:
            print(NumbersList[8])
    else:
        print("It is not a number!") 
else:
    print("Your input is out of range or even is not a number")  

        