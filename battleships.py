def print_grid(grid_value):
    key = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
    
    for i in range(10):
        if i == 0:
            print(f'  {i}', end='')
        if i != 9 and i != 0:
            print(f' {i}', end='')
        elif i == 9:
            print(f' {i}')
            

    for letter in range(10):
        print(f'{key[letter]} ', end='')
        for values in range(10):
            index_value=(letter*10)+values
            if values!=9:
                print(f'{grid_value[index_value]}|', end='')
            elif values==9:
                print(f'{grid_value[index_value]}|')
                
                
                

def main(args):
    player_grid = [' ']*100 # create list with default value ' '
    pc_grid = [' ']*100 # create list with default value ' '
    
    player_grid[0] = 0
    player_grid[1] = 1
    player_grid[99] = 'x'
    
    pc_grid[0] = 5
    pc_grid[99] = 'v'
    
    print_grid(player_grid) # print_grid
 
    print_grid(pc_grid)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    
