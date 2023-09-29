#input check
Test = False
while Test==False:
    try:
        n=int(input())
        Test=True
    except ValueError:
        print('Your input value is not a number. Try again.')

#sieve of Eratosthenes      
a=list(range(2,n+1))
b=a[:]
for i in range(0,len(a)):
    number=2*b[i]
    if b[i] in a:
        while number <= a[-1]:
            if number in a:
                a.remove(number)
                number+=b[i]
            else:
                number+=b[i]
    else:
        pass
print(a)