

def maze_solver(M,N,maze):

    solution = [ [0 for j in range(N)] for i in range(M)]
    

    print (solution)



if __name__ == "__main__":



    maze = [[1,0,1,0,0],
            [1,1,0,1,0],
            [0,1,0,0,0],
            [0,1,1,1,0],                
            [0,1,1,1,0],                
            [0,1,1,1,0],                
            [0,1,1,1,0],                
            [0,1,1,1,0],                
            [0,1,1,1,0],                
            [0,1,1,1,0],                
            ] 

            
    print (maze)
    M = 10
    N = 5
    maze_solver(M,N,maze)