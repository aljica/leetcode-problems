import sys

class Cipher:
	ROW, COL = 5, 5

	def __init__(self, key_phrase, plain_texts):
		self.key_phrase = key_phrase
		self.plain_texts = plain_texts


	def checkIfUsed(self, c, row, col):
		try:
			used = self.already_visited[c]
		except KeyError:
			self.key_table[row].append(c)
			self.already_visited[c] = (row, col)
			col += 1
		return col

	
	def createKeyTable(self):
		self.key_table = [[], [], [], [], []]
		self.already_visited = {}
		row, col = 0, 0
		for c in self.key_phrase:
			if col == Cipher.COL: 
				col = 0
				row += 1
			
			if c == ' ': continue
			c = c.upper()
			if c == 'J': c = 'I'
			
			col = self.checkIfUsed(c, row, col)
		
		start = ord('A')
		for i in range(ord('A'), ord('Z') + 1, 1):
			if col == Cipher.COL:
				col = 0
				row += 1
			
			c = chr(i)
			if c == 'J': continue

			col = self.checkIfUsed(c, row, col)

		return self.key_table
	

	def encode(self, x, y):
		if x == y and x == 'X': return 'Y', 'Y'
		encoded_x, encoded_y = '', ''

		row_x, col_x = self.already_visited[x][0], self.already_visited[x][1]
		row_y, col_y = self.already_visited[y][0], self.already_visited[y][1]
		
		if row_x == row_y:
			encoded_x = self.key_table[row_x][(col_x + 1) % Cipher.COL]
			encoded_y = self.key_table[row_y][(col_y + 1) % Cipher.COL]
		elif col_x == col_y:
			encoded_x = self.key_table[(row_x + 1) % Cipher.ROW][col_x]
			encoded_y = self.key_table[(row_y + 1) % Cipher.ROW][col_y]
		else:
			encoded_x = self.key_table[row_x][col_y]
			encoded_y = self.key_table[row_y][col_x]
		return encoded_x, encoded_y
	

	def encrypt(self):
		self.cipher_texts = []
		self.cipher_text = ""
		x, y = None, None
		encoded_x, encoded_y = None, None
		for plain_text in self.plain_texts:
			for c in plain_text:
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
				x, y = None, None
			self.cipher_texts.append(self.cipher_text)
			self.cipher_text = ""
		return self.cipher_texts
	

	def solve(self):
		self.createKeyTable()
		return self.encrypt()




def main():
	while True:
		n = int(sys.stdin.readline().strip())
		if n == 0: break
		key_phrase = sys.stdin.readline().strip()
		plain_texts = []
		plain_text = ""
		for i in range(n):
			plain_text += sys.stdin.readline().strip()
			plain_texts.append(plain_text)
			plain_text = ""
		cipher = Cipher(key_phrase, plain_texts)
		cipher_texts = cipher.solve()
		for cipher_text in cipher_texts:
			print(cipher_text)
		print()


if __name__ == "__main__":
	main()
