import math
from queue import PriorityQueue

class AStar:
	def __init__(self, grid, height, width):
		self.maze = []
		self.start = (0, 0)
		self.end = (height - 1, width - 1)

		for row, line in enumerate(grid):
			self.maze.append([])

			for column, state in enumerate(line):
				self.maze[row].append(Node(row, column, int(state)))

		self.maze[0][0].g_score = 0
		self.maze[0][0].f_score = self.manhatan_distance(self.start, self.end)

		for row in self.maze:
			for node in row:
				if node.is_open():
					node.update_neighbors(self.maze)

	def manhatan_distance(self, a, b):
		return abs(a[0] - b[0]) + abs(a[1] - b[1])

	def reconstruct_path(self, came_from, current):
		path = [ [0] * (self.end[1] + 1) for _ in range(self.end[0] + 1) ]

		while current in came_from:
			path[current[0]][current[1]] = 1
			current = came_from[current]

		path[0][0] = 1

		return path

	def solve(self):
		count = 0
		open_set = PriorityQueue()
		open_set.put((self.maze[0][0], count))
		came_from = {}
		open_set_hash = {self.maze[0][0]}

		while not open_set.empty():
			current = open_set.get()[0]
			open_set_hash.remove(current)

			if current.is_end(self.end):
				return self.reconstruct_path(came_from, self.end)

			for neighbor in current.neighbors:
				temp_g_score = current.g_score + 1

				if temp_g_score < neighbor.g_score:
					came_from[neighbor.get_pos()] = current.get_pos()
					neighbor.g_score = temp_g_score
					neighbor.f_score = temp_g_score + self.manhatan_distance(neighbor.get_pos(), self.end)

					if neighbor not in open_set_hash:
						count += 1
						open_set.put((neighbor, count))
						open_set_hash.add(neighbor)

		return [ [0] * (self.end[1] + 1) for _ in range(self.end[0] + 1) ]


class Node:
	def __init__(self, row, col, state):
		self.row = row
		self.col = col
		self.g_score = float("inf")
		self.f_score = float("inf")
		self.state = state
		self.neighbors = []

	def get_pos(self):
		return self.row, self.col

	def is_barrier(self):
		return self.state == 0
	
	def is_open(self):
		return self.state == 1

	def is_end(self, end_node):
		return self.row == end_node[0] and self.col == end_node[1]

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