def evenQ(number):
    return number % 2 == 0

#input check
numbers=[]
for i in [1,2]:
    Test = False
    while Test == False:
        try:
            numbers.append(int(input(f"The {'first' if i==1 else 'second'} number value: ")))
            Test=True
        except ValueError:
            print(f'Your input for {"first" if i==1 else "second"} number is not a number. Try again.')
            
#binary algorithm
numbersOLD=numbers[:]
factor = 1
while True:
    
    if numbers[0]==numbers[1]:
        gcd=numbers[0]
        break
    if numbers[0]==0:
        gcd=numbers[1]
        break
    elif numbers[1]==0:
        gcd=numbers[0]
        break
    
    if numbers[0]==1:
        gcd=1
    elif numbers[1]==1:
        gcd=1
        
    if evenQ(numbers[0]) == evenQ(numbers[1]):
        if evenQ(numbers[0]) == True:
            numbers[0]/=2
            numbers[1]/=2
            factor*=2  
        else:
            if numbers[1] > numbers[0]:
                numbers[1]=(numbers[1]-numbers[0])/2
            else:
                numbers[0]=(numbers[0]-numbers[1])/2          
    else:
        if evenQ(numbers[0]) == True:
            numbers[0]/=2
        else:
            numbers[1]/=2
    
print("The greatest common divisor of ", numbersOLD[0], " and ", numbersOLD[1], " is ", gcd*factor)