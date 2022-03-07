import sys


class DFS:
	def __init__(self, max_rows, max_cols, grid, queries):
		self.max_rows = max_rows
		self.max_cols = max_cols
		self.grid = grid
		self.queries = queries
	

	def getValueInCell(self, row, col):
		return self.grid[row][col]


	def extractQueryInfo(self, query):
		start_row, start_col = query[0], query[1]
		end_row, end_col = query[2], query[3]
		start_val = self.getValueInCell(start_row, start_col)
		end_val = self.getValueInCell(end_row, end_col)
		return start_row, start_col, start_val, end_row, end_col, end_val
	

	def move(self, row, col, val):
		if row > self.max_rows or row < 0 or col > self.max_cols or col < 0: return False
		coordinates = (row, col)
		new_val = self.getValueInCell(row, col)
		if new_val != val: return False
		try:
			visited = self.already_visited[coordinates]
		except KeyError:
			self.stack.append(coordinates)
			self.already_visited[coordinates] = new_val


	def dfs(self, query):
		start_row, start_col, start_val, end_row, end_col, end_val = self.extractQueryInfo(query)
		if start_val != end_val: return -1

		self.already_visited = {}
		self.stack = [(start_row, start_col)] # For DFS. LIFO: Append & pop from last index because those operations are O(1).

		while self.stack != []:
			current_cell = self.stack.pop(len(self.stack) - 1)
			current_row, current_col = current_cell[0], current_cell[1]
			current_val = self.getValueInCell(current_row, current_col)
			self.already_visited[(current_row, current_col)] = current_val
			if (current_row, current_col) == (end_row, end_col): return current_val

			# Find neighbors
"""
			# Quadrant 1
			if current_row < end_row and current_col > end_col:
				# Go right
				self.move(current_row, current_col + 1, current_val)
				# Go up
				self.move(current_row + 1, current_col, current_val)
				# Go left
				self.move(current_row, current_col - 1, current_val)
				# Go down
				self.move(current_row - 1, current_col, current_val)
				# Prioritize going down and left
			elif current_row < end_row and current_col < end_col:
				# Go up
				self.move(current_row + 1, current_col, current_val)
				# Go left
				self.move(current_row, current_col - 1, current_val)
				# Go right
				self.move(current_row, current_col + 1, current_val)
				# Go down
				self.move(current_row - 1, current_col, current_val)
				# Prioritize going down and right
			elif current_row > end_row and current_col > end_col:
				# Go right
				self.move(current_row, current_col + 1, current_val)
				# Go down
				self.move(current_row - 1, current_col, current_val)
				# Go up
				self.move(current_row + 1, current_col, current_val)
				# Go left
				self.move(current_row, current_col - 1, current_val)
			elif current_row > end_row and current_col < end_col:
				# Go down
				self.move(current_row - 1, current_col, current_val)
				# Go left
				self.move(current_row, current_col - 1, current_val)
				# Go right
				self.move(current_row, current_col + 1, current_val)
				# Go up
				self.move(current_row + 1, current_col, current_val)
			elif current_row > end_row and current_col == end_col:
				# Prioritize going up
				# Go down
				self.move(current_row - 1, current_col, current_val)
				# Go left
				self.move(current_row, current_col - 1, current_val)
				# Go right
				self.move(current_row, current_col + 1, current_val)
				# Go up
				self.move(current_row + 1, current_col, current_val)
			elif current_row < end_row and current_col == end_col:
				# Prioritize going down
				# Go left
				self.move(current_row, current_col - 1, current_val)
				# Go right
				self.move(current_row, current_col + 1, current_val)
				# Go up
				self.move(current_row + 1, current_col, current_val)
				# Go down
				self.move(current_row - 1, current_col, current_val)
			elif current_row == end_row and current_col < end_col:
				# Go left
				self.move(current_row, current_col - 1, current_val)
				# Go up
				self.move(current_row + 1, current_col, current_val)
				# Go down
				self.move(current_row - 1, current_col, current_val)
				# Go right
				self.move(current_row, current_col + 1, current_val)
			elif current_row == end_row and current_col > end_col:
				# Go up
				self.move(current_row + 1, current_col, current_val)
				# Go down
				self.move(current_row - 1, current_col, current_val)
				# Go right
				self.move(current_row, current_col + 1, current_val)
				# Go left
				self.move(current_row, current_col - 1, current_val)"""
			






			# Go right or left first?
			"""
			if current_row > end_row:
				# Go right
				self.move(current_row, current_col + 1, current_val)
				# Go left (this will be enqueued later, which means we'll visit this one sooner)
				self.move(current_row, current_col - 1, current_val)
			else:
				# Go left
				self.move(current_row, current_col - 1, current_val)
				# Go right
				self.move(current_row, current_col + 1, current_val)

			if current_col > end_col:
				# Go up
				self.move(current_row + 1, current_col, current_val)
				# Go down
				self.move(current_row - 1, current_col, current_val)
			else:
				# Go down
				self.move(current_row - 1, current_col, current_val)
				# Go up
				self.move(current_row + 1, current_col, current_val)
				"""

			

			# Go right
			self.move(current_row, current_col + 1, current_val)
			# Go left
			self.move(current_row, current_col - 1, current_val)
			# Go up
			self.move(current_row + 1, current_col, current_val)
			# Go down
			self.move(current_row - 1, current_col, current_val)
		return -1


	def handleQueries(self):
		for query in self.queries:
			result = self.dfs(query)
			if result == -1: print("neither")
			elif result == 0: print("binary")
			elif result == 1: print("decimal")


def main():
	size = sys.stdin.readline().strip().split()
	grid_row, grid_col = int(size[0]), int(size[1])
	grid = []
	for i in range(grid_row):
		grid.append([])
		line = sys.stdin.readline().strip()
		for element in line:
			grid[i].append(int(element))
	
	num_queries = int(sys.stdin.readline().strip())
	queries = []
	for i in range(num_queries):
		query = sys.stdin.readline().strip().split(' ')
		queries.append([(int(element) - 1) for element in query])

	dfs = DFS(grid_row - 1, grid_col - 1, grid, queries)
	dfs.handleQueries()



if __name__ == "__main__":
	main()
