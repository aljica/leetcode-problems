import sys

class Cipher:
	def __init__(self, key_phrase, plain_text):
		self.key_phrase = key_phrase
		self.plain_text = plain_text

	
	def createKeyTable(self):
		self.key_table = [[], [], [], [], []]
		self.already_visited = {}
		row, col = 0, 0
		for c in self.key_phrase:
			if col == 5: 
				col = 0
				row += 1
			
			if c == ' ': continue
			c = c.upper()
			if c == 'J': c = 'I'
			
			# Check if c has already been used
			try:
				used = self.already_visited[c]
				continue
			except KeyError: pass

			# Otherwise, add it
			self.key_table[row].append(c)
			self.already_visited[c] = (row, col)

			col += 1
		
		start = ord('A')
		for i in range(ord('A'), ord('Z') + 1, 1):
			if col == 5:
				col = 0
				row += 1
			
			letter = chr(i)
			if letter == 'J': continue

			try:
				used = self.already_visited[letter]
				continue
			except KeyError: pass

			self.key_table[row].append(letter)
			self.already_visited[letter] = (row, col)

			col += 1

		
		return self.key_table
	

	def encode(self, x, y):
		if x == y and x == 'X': return 'Y', 'Y'
		encoded_x, encoded_y = '', ''

		row_x, col_x = self.already_visited[x][0], self.already_visited[x][1]
		row_y, col_y = self.already_visited[y][0], self.already_visited[y][1]
		
		if row_x == row_y:
			encoded_x = self.key_table[row_x][(col_x + 1) % 5]
			encoded_y = self.key_table[row_y][(col_y + 1) % 5]
		elif col_x == col_y:
			encoded_x = self.key_table[(row_x + 1) % 5][col_x]
			encoded_y = self.key_table[(row_y + 1) % 5][col_y]
		else:
			encoded_x = self.key_table[row_x][col_y]
			encoded_y = self.key_table[row_y][col_x]
		return encoded_x, encoded_y
	

	def encrypt(self):
		self.cipher_text = ""
		x, y = None, None
		encoded_x, encoded_y = None, None
		for c in self.plain_text:
			if c == ' ': continue
			c = c.upper()
			if c == 'J': c = 'I'

			if not x: x = c
			else:
				y = c
				if x == y:
					encoded_x, encoded_y = self.encode(x, 'X')
					x, y = y, None
				else:
					encoded_x, encoded_y = self.encode(x, y)
					x, y = None, None
				self.cipher_text += encoded_x + encoded_y
		if x:
			encoded_x, encoded_y = self.encode(x, 'X')
			self.cipher_text += encoded_x + encoded_y
		return self.cipher_text
	

	def solve(self):
		self.createKeyTable()
		self.encrypt()




def main():
	while True:
		n = int(sys.stdin.readline().strip())
		if n == 0: break
		key_phrase = sys.stdin.readline().strip()
		plain_text = ""
		for i in range(n):
			plain_text += sys.stdin.readline().strip()
		cipher = Cipher(key_phrase, plain_text)
		cipher.solve()


if __name__ == "__main__":
	main()
