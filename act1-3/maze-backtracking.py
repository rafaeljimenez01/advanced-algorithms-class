

def maze_solver(M, N, maze):

    maze_helper = maze

    solution = [ [0 for j in range(N)] for i in range(M)]
    
    max_size_y = M
    max_size_x = N


    def helper(x, y, maze_helper, solution):

        if x == max_size_x - 1 and y == max_size_y - 1 and maze_helper[y][x] == 1:

            solution[y][x] = 1
            return True

        if x >= 0 and x < max_size_x and y >= 0 and y < max_size_y and maze_helper[y][x] == 1:
             # mark x, y as part of solution path
            
            if solution[y][x] == 1:
                return False
            
            solution[y][x] = 1
            
            # Move forward in x direction
            if helper(x + 1, y, maze, solution) == True:
                return True
                
            # If moving in x direction doesn't give solution
            # then Move down in y direction
            if helper(x, y + 1, maze,  solution) == True:
                return True
            
            # If moving in y direction doesn't give solution then
            # Move back in x direction
            if helper(x - 1, y, maze, solution) == True:
                return True
                
            # If moving in backwards in x direction doesn't give solution
            # then Move upwards in y direction
            if helper(x, y - 1, maze, solution) == True:
                return True
            
            # If none of the above movements work then
            # BACKTRACK: unmark x, y as part of solution path
            solution[y][x] = 0
            return False

    helper(0,0, maze_helper, solution)


    print(solution)
    

 

if __name__ == "__main__":

    with open("tests.txt") as reader:
        M = int(reader.readline())
        N = int(reader.readline())		

        lines = reader.readlines()

        
        lines = [line.rstrip().split() for line in lines]
        
        maze = []
        for line in lines:
            maze.append([int(num) for num in line])

    maze_solver(M,N,maze)