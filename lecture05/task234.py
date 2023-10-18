#Due to the fact that task 4 is generalization of task 2 and task 1, I have decided to create just one file for all of them

import functions_for_tasks_2_3_4 as f

dice_list = f.DiceInput()
    
for dice in range(0,len(dice_list)):
    print(f'%%%%%%%%%% The {"first" if dice == 0 else "second" if dice == 1 else "third" if dice == 2 else dice }-dice combination ({dice_list[dice][0]}d{dice_list[dice][1]}) %%%%%%%%%%')
    print('         My code:               random module:')
    probability_list = f.DiceProbabilityList(int(dice_list[dice][0]),int(dice_list[dice][1]))
    r_probability_list = f.DiceRandom(int(dice_list[dice][0]),int(dice_list[dice][1]),100000)
    for number in range(0,len(probability_list)):
        print(f'{number+1} =    {round(probability_list[number], 3)}',f'{round(r_probability_list[number], 3)}',sep='                       ')