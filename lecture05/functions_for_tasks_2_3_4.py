def DiceInput() -> list:
    """
        Dice input check
         
        Validating that user's input has the following form:
        "#d# #d#..."
        Otherwise, repeating input procedure
        
        Returns the user's input
    """

    from re import split, findall

    Test = False
    while Test == False:
        dice_input = input('Input your dices in following form:\n#d# #d# #d#...\nwhere dices are separated by space:\n')
        dice_list = findall(r'\d{1,}[d]\d{1,}', dice_input)

        Test = split(r'\s', dice_input) == dice_list
        
        if Test == True:
            n_dice_list = []
            for i in range(0,len(dice_list)):
                n_dice_list = n_dice_list + [dice_list[i].split('d')]
                
        else: print("Your input is incorrect. Please try again")
        
    return n_dice_list


def DiceProbabilityList(Number_of_Dice: int, Dice_Type: int) -> list:
    """
    Dice roll probability

    Args:
        Number_of_Dice (int): Number of particular dice
        Dice_Type (int): Type of dice, like 2 for d2 or 4 for d4 and e.t.c
        
    Returns probability list
    """
    
    #Cartesian product
    def recursion(c_list,n_list, DiceCounter):
        DiceCounter-=1
        ilist = [[c_list[k]+n_list[j] for j in range(0,len(n_list))] for k in range(0,len(c_list))]
        ilist1 = []
        for i in ilist:
            ilist1+=i
        
        ilist2 = ilist1[:]
        if DiceCounter > 0:
            ilist2 = recursion(ilist1,n_list,DiceCounter)
            
        return ilist2
    
    #Number of occurrences of each result
    def number_of_occurrences(p_list):
        coeff_list = [0 for i in range(0,Number_of_Dice*Dice_Type)]
        for i in range(1,Number_of_Dice*Dice_Type+1):
            for j in p_list:
                if j == i:
                    coeff_list[j-1]+=1
                    
        return coeff_list
    
    #Probability calculation
    def probability(o_list):
        
        def division(number: int):
            return number/(Dice_Type**Number_of_Dice)*100
        
        return list(map(division,o_list))

    return probability(number_of_occurrences(recursion([0], list(range(1,Dice_Type+1)), Number_of_Dice)))


def DiceRandom(Number_of_Dice: int, Dice_Type: int, Number_of_Rolls: int) -> list:
    """Dice roll probabiliy via random module

    Args:
        Number_of_Dice (int): Number of particular dice
        Dice_Type (int): Type of dice, like 2 for d2 or 4 for d4 and e.t.c
        Number_of_Rolls (int): number of rolls

    Returns:
        list: _description_
    """
    from random import randint
    r_list = [0 for i in range(0,Number_of_Dice*Dice_Type)]
    
    for roll in range(0,Number_of_Rolls):
        number = []
        for dice in range(0,Number_of_Dice):
            number.append(randint(1,Dice_Type))
            
        for i in range(1,Number_of_Dice*Dice_Type+1):
                if sum(number) == i:
                    r_list[i-1]+=1
                    
    #Probability calculation
    def probability(o_list):
        
        def division(number: int):
            return number/(Number_of_Rolls)*100
        
        return list(map(division,o_list))
                  
    return probability(r_list)

