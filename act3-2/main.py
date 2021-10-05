import heapq
from os import read

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


# INPUT:
#   - graph: dictionary of dictionaries.
#   - origin: int
# OUTPUT:
#   - dictionary of dictionaries.
# DESCRIPTION:
#   Finds shortest path to each and every node from a common origin.
# Time Complexity: 
#   O(V^2) where V is the number of nodes.
# Space Complexity:
#   O((E * V) * V) where V is the number of nodes and E is the number of edges.
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
# INPUT:
#   - graph: dictionary of dictionaries.
# OUTPUT:
#   - none.
# DESCRIPTION:
#   Prints the distnace from very node to every other node.
# Time Complexity: 
#   O(V^2) where V is the number of nodes.
# Space Complexity:
#   O(1)
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
    #Value used to fill in matrix when there is no connection between two nodes
    INF = float('inf')
    # Dictionary that stores another dictionary to map a node with its neighbors
    # and the distance from each other.
    # (e.g {node: {neighbor_1: dist, neighbor_2: dist, ...}})
    graph_dict = {}
    # Matrix created to read the txt as an adjency matrix
    graph_matrix = []
    # Dictionary that stores another dictionary to map a node with all other
    # neighbors and the shortest distance to travel to each other.
    # (e.g {node: {neighbor_1: dist, neighbor_2: dist, ...}})
    solution = {}

    # Open file to load graph.
    with open("test.txt") as reader:
        number = 0
        size = reader.readline()

        while size != '':
            number += 1
            print("test {number}:\n".format(number=number))
            # Iterates for all nodes.
            for node in range(int(size)):
                # Initiate current node's neighbor dictionary.
                graph_dict.update({node: {}})
                # Initiate row to read the graph as a matrix
                current_row = []
                # Populate current node's neighbors dictionary.
                for neighbor, distance in enumerate(reader.readline().split(' ')):
                    if int(distance) != -1 and neighbor != node:
                        graph_dict[node][neighbor] = int(distance)

                    # When there is no connection between nodes we prefer 
                    # to use infinite value so the algorithms logic is simpler
                    if int(distance) == -1:
                        current_row.append(INF)
                    else:
                        current_row.append(int(distance))
                        
                #Populate matrix
                graph_matrix.append(current_row)
            # Run dijkstra algorithim for every node as origin.
            for node in graph_dict.keys():
                # Populate solution
                solution.update({node: dijksra(graph_dict, node)})

            #Print dijkstra so it is easily readable
            print_dijkstra(solution)
            #Run floyd for current graph
            print_floyd(floyd(graph_matrix))
            # Set up for next iteration if any.
            graph_matrix = []
            solution = {}
            print("\n\n")
            size = reader.readline()        

        