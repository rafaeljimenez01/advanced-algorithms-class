

def maze_solver(M, N, maze):

    #create a copy to use it in the helper function
    maze_helper = maze

    #creates 2D array that will show you the correct path
    solution = [ [0 for j in range(N)] for i in range(M)]
    

    #Use the size of array to create limits
    max_size_y = M
    max_size_x = N


    #Helper function
    #This function it's in charge of the recursive portion of the algorith
    #Time complexity:   O(4^n) because for each step of the maze, the recursion tree can take 4 different choices
    #Space complexity: O(n*n) because the solution matrix depends solely on the size of the input 
    ###### Base con the rat in a maze code in gfg https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/

    def helper(x, y, maze_helper, solution):

        if x == max_size_x - 1 and y == max_size_y - 1 and maze_helper[y][x] == 1:

            solution[y][x] = 1
            return True

        if x >= 0 and x < max_size_x and y >= 0 and y < max_size_y and maze_helper[y][x] == 1:
            
            #checks if this is already part of the solution 
            
            if solution[y][x] == 1:
                return False
            
            #adds the current indexes as part of the path
            solution[y][x] = 1
            
            # Moves to the right 
            if helper(x + 1, y, maze, solution) == True:
                return True
                
            # If moving to the right didn't solved the maze, move bottom 
            if helper(x, y + 1, maze,  solution) == True:
                return True
            
            #If moving to the bottom didn't solved the maze, move left

            if helper(x - 1, y, maze, solution) == True:
                return True
                
            #If moving to the left didn't solved the maze, move top
            
            if helper(x, y - 1, maze, solution) == True:
                return True
            
            # If not solved unmark current position and return False, because the path was not found
            solution[y][x] = 0
            return False

    #Call the helper function starting in the top left position 
    helper(0,0, maze_helper, solution)


    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in solution]))
    

 

if __name__ == "__main__":

    '''
    First test case

    This test case, checks if the backtracking it's correct because of the order of decision
    the algorithm will find a dead end and will have to backtrack 4 steps checking if the recursion 
    is well structured

    ''' 

    print("First test case")
    with open("tests.txt") as reader:
        M = int(reader.readline())
        N = int(reader.readline())		

        lines = reader.readlines()

        
        lines = [line.rstrip().split() for line in lines]
        
        maze = []
        #creates a 2D array with the input in the txt
        for line in lines:
            maze.append([int(num) for num in line])

    maze_solver(M,N,maze)
    
    
    '''
    Second test case

    Checks if the algorithm does not has problems when having to move up 

    '''
    print("Second test case")
    with open("tests1.txt") as reader:
        M = int(reader.readline())
        N = int(reader.readline())		

        lines = reader.readlines()

        
        lines = [line.rstrip().split() for line in lines]
        
        maze = []
        #creates a 2D array with the input in the txt
        for line in lines:
            maze.append([int(num) for num in line])

    maze_solver(M,N,maze)
    '''
    Third test case
    
    No solution test case, test if even having the option to cycle the algorithm won't
    
    '''
    print("Third test case")
    with open("tests2.txt") as reader:
        M = int(reader.readline())
        N = int(reader.readline())		

        lines = reader.readlines()

        
        lines = [line.rstrip().split() for line in lines]
        
        maze = []
        #creates a 2D array with the input in the txt
        for line in lines:
            maze.append([int(num) for num in line])

    maze_solver(M,N,maze)
    '''
    Fourth test case

    Checks if the algorithm it's in fact taking the first possible option, 
    so the algorithm it's the most time efficient possible 

    '''

    print("Fourth test case")
    with open("tests3.txt") as reader:
        M = int(reader.readline())
        N = int(reader.readline())		

        lines = reader.readlines()

        
        lines = [line.rstrip().split() for line in lines]
        
        maze = []
        #creates a 2D array with the input in the txt
        for line in lines:
            maze.append([int(num) for num in line])

    maze_solver(M,N,maze)