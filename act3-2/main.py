import sys


def relax(u, v, distance, current_cost):
    pass

def dijkstra(adjacency_matrix, origin):
    pass

if __name__ == "__main__":
    adjacency_matrix = []

    for _ in range(int(input())):
        row = input().split(' ')
        adjacency_matrix.append([int(edge) for edge in row])
