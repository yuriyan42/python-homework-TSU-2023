from random import randint

#bubble sort function
def BubSort(o_list):
    i_list = o_list[:]
    number_of_comparisons = 1
    while number_of_comparisons !=0:
        number_of_comparisons=0
        for i in range(0,len(i_list)-1):
            if i_list[i] > i_list[i+1]:
                i_list[i], i_list[i+1] = i_list[i+1], i_list[i]
                number_of_comparisons+=1
            
    return i_list

    
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
r_list=[randint(-10000,10000) for i in range(0,length)]
print('Original list: ', r_list)

#bubble sorted list print
print('Bubble sorted list: ', BubSort(r_list))
