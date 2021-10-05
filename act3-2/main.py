import heapq

'''

Dijkstra and Floyd implementations

Advanced algorithms class

Authors:

Rafael Jimenez A01637850
Joshua Hernandez A01


'''

####################

#Floyd-Warshall algorithm -Based on GfG https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
#Finds the sortest paths in a directed and weightyed graph
#Input: Graph (adjency matrix)
#Output: 2x2 matrix with the shortest paths(similar to adjency matrix but with shortest paths)
#Time complexity: O(V^3) where V is the number of vertices the graph has

####################

def floyd(graph): 

    # This will initialize the result matrix, and will contain the 
    # sortest distances between every pair of vertices
    V = len(graph)
    solution = graph
    

    #We will take every possible vertex as an intermediate vertex, named K
    for k in range(V):
 
        # We will take i as the soruce vertex (from where the path would begin)
        for i in range(V):
 
            # We will take j as the vertex of destination for every i(source)
            for j in range(V):
 
                # We can make two decisions, to take the k intermidiate vertex 
                # of to skip it. We will take it into account only if the k vertex
                # is part of the shortest path

                if solution[i][k] + solution[k][j] < solution[i][j]:
                    solution[i][j] = solution[i][k] + solution[k][j]
                                

    return solution


def dijksra(graph, origin):
    # Dictionary that stores another dictionary to map a node with all other
    # neighbors and the shortest distance to travel to each other.
    # (e.g {node: {neighbor_1: dist, neighbor_2: dist, ...}})
    distances = {node: float('inf') for node in graph}
    # tuple's list that holds the nodes to be vistied. Each tuple holds the 
    # distance to the node from the origin and the node to be visited. The order
    # in which the nodes will be visited depend on the distance value.
    priority_queue = [(0, origin)]
    
    # Distance from  oirign to itlsef set to 0.
    distances[origin] = 0

    # Iterate through priority queue until empty.
    while priority_queue:
        # Pop node with smallest distance.
        current_distance, current_node = heapq.heappop(priority_queue)

        # Only analize node if the distance to current node is not grater.  
        if current_distance <= distances[current_node]:
            for neighbor, traveled_distance in graph[current_node].items():
                distance = current_distance + traveled_distance

                # Only consider current path if it's better than any path analyzed
                # befoire
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances


'''
Functions used to format the output so it is easily readable
'''
def print_dijkstra(graph):
    # Print's header.
    print("Dijkstra:")

    # Prints distance from every node to every node.
    for origin in graph.keys():
        for end in graph[origin].keys():
            if origin != end:
                print("node {origin} to node {end}: {min_distance}".format(
                    origin=origin+1, end=end+1, min_distance=graph[origin][end])
                )

def print_floyd(graph):
    print("\nFloyd:")
    #Python oneliner to print the matrix in a 2D way so its easier to read
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])  
      for row in graph]))

if __name__ == "__main__":
    
    # Dictionary that stores another dictionary to map a node with its neighbors
    # and the distance from each other.
    # (e.g {node: {neighbor_1: dist, neighbor_2: dist, ...}})
    graph = {}
    # Dictionary that stores another dictionary to map a node with all other
    # neighbors and the shortest distance to travel to each other.
    # (e.g {node: {neighbor_1: dist, neighbor_2: dist, ...}})
    solution = {}

    # Open file to load graph.
    with open("test.txt") as reader:
        # Iterates for all nodes.
        for node in range(int(reader.readline())):
            # Initiate current node's neighbor dictionary.
            graph |= {node: {}}

            # Populate current node's neighbors dictionary.
            for neighbor, distance in enumerate(reader.readline().split(' ')):
                if distance != "-1" and neighbor != node:
                    graph[node][neighbor] = int(distance)

        # Run dijkstra algorithim for every node as origin.
        for node in graph.keys():
            # Populate solution
            solution |= {node: dijksra(graph, node)}
        
        INF = float('inf')
        
        #First test case, used to verify that the algorithms are working properly since
        #we have a correct output to compare to
        graph_test = [[0, 2, INF, 3],
        [INF, 0, 1, 5],
        [2, 3, 0,   INF],
        [3, INF, 4, 0]
        ]

        #Second test case, 
        graph_test1 = [[0, 2, INF],
        [INF, 0, 3],
        [4, INF, 0],
        ]

        print_dijkstra(solution)
        print_floyd(floyd(graph_test))
        print_floyd(floyd(graph_test1))
