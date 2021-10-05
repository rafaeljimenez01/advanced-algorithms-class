import heapq
from os import read

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
        number = 0
        size = reader.readline()

        while size != '':
            number += 1
            print("test {number}:\n".format(number=number))
            # Iterates for all nodes.
            for node in range(int(size)):
                # Initiate current node's neighbor dictionary.
                graph.update({node: {}})

                # Populate current node's neighbors dictionary.
                for neighbor, distance in enumerate(reader.readline().split(' ')):
                    if int(distance) != -1 and neighbor != node:
                        graph[node][neighbor] = int(distance)

            # Run dijkstra algorithim for every node as origin.
            for node in graph.keys():
                # Populate solution
                solution.update({node: dijksra(graph, node)})

            print_dijkstra(solution)

            # Set up for next iteration if any.
            print("\n\n")
            size = reader.readline()