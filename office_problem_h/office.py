import sys


class Office:
	
	def __init__(self, w, h, employee_names, employee_spaces):
		self.w = w
		self.h = h
		self.employee_names = employee_names
		self.employee_spaces = employee_spaces

		self.total = self.w * self.h
		self.unallocated = self.w * self.h
		self.contested = 0
		self.guaranteed = [0] * len(self.employee_names)

		self.grid = {}
	

	def encode(self, SW, NE, employee_i):
		for x in range(SW[0], NE[0], 1):
			for y in range(SW[1], NE[1], 1):
				try:
					lst = self.grid[(x, y)]
					lst.append(employee_i)
					if len(lst) == 2: 
						self.contested += 1
						for employee in lst: self.guaranteed[employee] -= 1
					else:
						self.guaranteed[employee_i] -= 1
				except KeyError:
					self.grid[(x, y)] = [employee_i]

						
	def calculateGuaranteed(self, SW, NE, employee_i):
		self.guaranteed[employee_i] = (NE[0] - SW[0]) * (NE[1] - SW[1])
	
	
	def encodeAllEmployees(self):
		for i in range(len(self.employee_spaces)):
			SW = self.employee_spaces[i][0] # Tuple (x, y)
			NE = self.employee_spaces[i][1]
			
			self.calculateGuaranteed(SW, NE, i)
			self.encode(SW, NE, i)
		
		self.unallocated -= len(self.grid)
		print("Total", self.total)
		print("Unallocated", self.unallocated)
		print("Contested", self.contested)
		for i in range(len(self.employee_names)):
			print(self.employee_names[i], self.guaranteed[i])


def main():
	while True:
		size = sys.stdin.readline().strip().split()
		if not size: break
		w, h = int(size[0]), int(size[1])
		num_emp = int(sys.stdin.readline().strip())
		employees = []
		employee_spaces = []
		for i in range(num_emp):
			data = sys.stdin.readline().strip().split()
			employees.append(data[0])
			start_coordinate = int(data[1]), int(data[2])
			end_coordinate = int(data[3]), int(data[4])
			employee_spaces.append((start_coordinate, end_coordinate))
		office = Office(w, h, employees, employee_spaces)
		office.encodeAllEmployees()


if __name__ == "__main__":
	main()
