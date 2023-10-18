Test = False
try:
    input = open('task1.txt')
    Test = True
except FileNotFoundError:
    print('Your input file has to be placed into working directory with name "task1.txt"')
if Test == True:
    n_list = list(map(int, input.readlines()))
        
    numbers_list = []
    for i in range(0,len(n_list)):
        for j in range(0,len(n_list)):
            for k in range(0,len(n_list)):
                if n_list[i] + n_list[j] + n_list[k] == 2020:
                    numbers_list.append(n_list[i] * n_list[j] * n_list[k])
                    
    numbers_list_without_duplicates = list(set(numbers_list))

    with open('output.txt','w') as output:
        for i in range(0,len(numbers_list_without_duplicates)):
            print(numbers_list_without_duplicates[i],file=output)