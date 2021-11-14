def print_grid(grid_value, hide_ships):
    # hide_ships == 1 hide value (ship for enemy) %
    # hide_ships == 0 not hide value (ship for enemy) %
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
                if grid_value[index_value] == '%' and hide_ships==1:
                    print(' |', end='')
                else:
                    print(f'{grid_value[index_value]}|', end='')
            elif values==9:
                if grid_value[index_value] == '%' and hide_ships==1:
                    print(' |')
                else:
                    print(f'{grid_value[index_value]}|')
                
                
                

def main(args):
    player_grid = [' ']*100 # create list with default value ' '
    pc_grid = [' ']*100 # create list with default value ' '
    
    player_grid[0] = 0
    player_grid[1] = 1
    player_grid[99] = '%'
    
    pc_grid[0] = 5
    pc_grid[99] = '%'
    
    print_grid(player_grid, 1) # print_grid
 
    print_grid(pc_grid, 1)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    
