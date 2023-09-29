def EnvAn(y,x):
    possibilities = []
    if maze[y][x-1] != '#':
        possibilities.append([y,x-1])
    if maze[y][x+1] != '#':
        possibilities.append([y,x+1])
    if maze[y-1][x] != '#':
        possibilities.append([y-1,x])
    if maze[y+1][x] != '#':
        possibilities.append([y+1,x])
    
    return possibilities

def step(pathlist, path_number, y, x, y_old, x_old):
    if [[y_old, x_old]] == EnvAn(y,x):
        maze[y][x] = "de"
        del pathlist[path_number]
        Exit = False
    elif [y, x] in [[0,0],[0,1],[1,0],[19,19],[19,18],[18,19]]:
        Exit = True
    else:
        for i in range(0, len(EnvAn(y,x))):
            if not(EnvAn(y,x)[i] in pathlist[path_number]):
                pathlist = pathlist + [pathlist[path_number] + [EnvAn(y,x)[i]]]
        del pathlist[path_number]
        Exit = False
    return pathlist, Exit


#labyrinth initialization
maze = [
    [' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' '],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' '],
]


#input check
coordinates=[]
size = len(maze)
for i in [1,2]:
    Test = False
    while Test == False:
        try:
            coordinates.append(int(input(f"The {'y' if i==1 else 'x'} coordinate value: 1")))
            range(0,len(maze))[coordinates[i-1]]
            Test=True
        except ValueError:
            print(f'Your input for {"y" if i==1 else "x"} coordinate is not a number. Try again.')
        except IndexError:
            print(f'Your input for {"y" if i==1 else "x"} coordinate is out of range {len(maze)}. Try again.')

            
#drawing initial picture
maze[coordinates[0]][coordinates[1]] = "++"

xi, yi = 0, 0
while yi < len(maze):
    print("".join(maze[yi]).replace("#", "██").replace(" ", "  "))
    yi += 1


#
pathlist=[[[coordinates[0], coordinates[1]],[coordinates[0], coordinates[1]],],]

Exit = False
while Exit == False:
    
    for j in range(0,len(pathlist)):
        if j < len(pathlist):
            (pathlist, Exit) = step(pathlist, j, pathlist[j][-1][0], pathlist[j][-1][1], pathlist[j][-2][0], pathlist[j][-2][1])

pathlengthlist = list(map(len, pathlist))

print('# of aviable paths is:', len(pathlist))
print("The shortest path's length is: ",min(pathlengthlist))   
