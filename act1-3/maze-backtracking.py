

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


    print(solution)
    

 

if __name__ == "__main__":

    #read the txt by lines 
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