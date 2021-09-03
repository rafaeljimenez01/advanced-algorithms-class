import math
from queue import PriorityQueue

class AStar:

	# INPUT: 
	#	- maze: 2D list
	# 	- height: integer
	#	- width: integer
	# OUTPUT: None.
	# Description: Initializes the maze filled with nodes in order to solve it.
	def __init__(self, grid, height, width):
		self.maze = []						# 2D array to hold the nodes.
		self.start = (0, 0)					# tuple with the upper left corner cordenates.
		self.end = (height - 1, width - 1)	# tulple with the lower right corner cordenates.

		# unwrapps the grid to generate a 2D list filled with Node objects.
		for row, line in enumerate(grid):
			self.maze.append([])

			for column, state in enumerate(line):
				self.maze[row].append(Node(row, column, int(state)))

		# Initialize start Node.
		self.maze[0][0].g_score = 0
		self.maze[0][0].f_score = self.manhatan_distance(self.start, self.end)

		# adds neighbors to each node.
		for row in self.maze:
			for node in row:
				if node.is_open():
					node.update_neighbors(self.maze)

	def manhatan_distance(self, a, b):
		return abs(a[0] - b[0]) + abs(a[1] - b[1])

	# INPUT: 
	#	- came_from: dict with tuple to tuple.
	#	- current: tuple with current node cordenates (only null when no solution).
	# OUTPUT: None
	# Description: Generates a 2D lsit of 0s and 1s to display solution.
	# TIME COMPLEXITY: O(h*w + p) where h is the maze height, w is the maze
	# width and p is the number of nodes for the solution.
	def reconstruct_path(self, came_from, current):
		path = [ [0] * (self.end[1] + 1) for _ in range(self.end[0] + 1) ]

		while current in came_from:
			path[current[0]][current[1]] = 1
			current = came_from[current]

		path[0][0] = 1

		return path

	# INPUT: None.
	# OUTPUT: 2D list of obejcts node.
	# DESCRIPTION: finds shortest path utilizing a brancha bound approach. Where
	# it checks the current node's neighbor choosing the to move to the 
	# best neighbor based on the current distance traveled plus the straight
	# between the possible future node and the end node.
	# TIME COMPLEXITY: O(E + reconstruct_path) where E is the number of edges.
	def solve(self):
		count = 0
		open_set = PriorityQueue()
		open_set.put((self.maze[0][0], count))
		came_from = {}
		open_set_hash = {self.maze[0][0]}

		# continues looking for a path while there is still possible future steps.
		while not open_set.empty():
			current = open_set.get()[0]
			open_set_hash.remove(current)

			# solution is found.
			if current.is_end(self.end):
				return self.reconstruct_path(came_from, self.end)

			# checks all neighbors as a future step.
			for neighbor in current.neighbors:
				temp_g_score = current.g_score + 1

				# bounds the future step to have a better score.
				if temp_g_score < neighbor.g_score:
					came_from[neighbor.get_pos()] = current.get_pos()
					neighbor.g_score = temp_g_score
					neighbor.f_score = temp_g_score + self.manhatan_distance(neighbor.get_pos(), self.end)

					# makes sure the node is not part of the path already to add it.
					if neighbor not in open_set_hash:
						count += 1
						open_set.put((neighbor, count))
						open_set_hash.add(neighbor)

		return self.reconstruct_path(came_from, current.get_pos())


class Node:
	def __init__(self, row, col, state):
		self.row = row				# y cordenate.
		self.col = col				# x cordente.
		self.g_score = float("inf")	# steps or distance already traveled.
		self.f_score = float("inf")	# distance between node and end node
		self.state = state			# describes if node is a barrier or open to travel through
		self.neighbors = []			# list of adjacent nodes.

	def get_pos(self):
		return self.row, self.col

	def is_barrier(self):
		return self.state == 0
	
	def is_open(self):
		return self.state == 1

	def is_end(self, end_node):
		return self.row == end_node[0] and self.col == end_node[1]

	# INPUT: maze: 2D list
	# OUTPUT: None
	# Description: checks all posible 4 neighbors for the node to add them as 
	# negihbors. 
	# NOTE: a node cannot be a neighbor if it's a barrier or the cordenates are
	# out of bound wiht respect to the maze's dimension.
	# Time complexity: O(1)
	def update_neighbors(self, maze):
		if self.row < len(maze) - 1 and not maze[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(maze[self.row + 1][self.col])

		if self.row > 0 and not maze[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(maze[self.row - 1][self.col])

		if self.col < len(maze) - 1 and not maze[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(maze[self.row][self.col + 1])

		if self.col > 0 and not maze[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(maze[self.row][self.col - 1])

	def __lt__(self, other):
		return False


def main():
	with open("tests.txt") as reader:
		height = int(reader.readline())
		width = int(reader.readline())		

		print(AStar([reader.readline()[:-1:2] for i in range(height)], height, width).solve())

main()