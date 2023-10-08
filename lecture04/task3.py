from random import shuffle, randint

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

#bogosort function
def BogSort(bs_list):
    i_list = bs_list[:]
    number_of_shuffles = 1
    while BubSort(i_list) != i_list:
        number_of_shuffles += 1
        shuffle(i_list)
   
    return i_list, number_of_shuffles
    
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

#bogosorted list print
(b_list, number_of_shuffles) = BogSort(r_list)
print('Bogosorted list: ', b_list)
print('Number of shuffles: ', number_of_shuffles)

    