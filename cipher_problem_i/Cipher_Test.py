import unittest
from Cipher import Cipher

class Cipher_Test(unittest.TestCase):

	#def setUp(self):
		#self.cipher = Cipher("", "")
	
	
	def test_createKeyTable(self):
		cipher = Cipher("hEllo    world", "")
		result = cipher.createKeyTable()
		expected = [['H', 'E', 'L', 'O', 'W'], ['R', 'D', 'A', 'B', 'C'], ['F', 'G', 'I', 'K', 'M'], ['N', 'P', 'Q', 'S', 'T'], ['U', 'V', 'X', 'Y', 'Z']]
		self.assertEqual(result, expected)
	

	def test_encode(self):
		cipher = Cipher("hEllo world", "")
		cipher.createKeyTable()
		result = cipher.encode("H", "Y")
		expected = ("O", "U")
		
		self.assertEqual(result, expected)
	

	def test_encrypt(self):
		cipher = Cipher("hEllo world", "stop that oo s")
		cipher.createKeyTable()
		result = cipher.encrypt()
		expected = "TNESNWCQLYBY"

		self.assertEqual(result, expected)

	@unittest.skip
	def test_encrypt(self):
		cipher = Cipher("Just another example", "Meet me at eight o clockSigned Agent Double O Eight")
		result = cipher.solve()
		expected = "LOLELOIANTFEUEGXNDCBTUCEOGTKROUGMOXBRHNTFEIL"

		self.assertEqual(result, expected)
	

	def test_encode(self):
		cipher = Cipher("Just another example", "Meet me at eight o clock\nSigned Agent Double O Eight\n")
		cipher.createKeyTable()
		result = cipher.encode("O", "C")
		expected = ("N", "D")
		
		self.assertEqual(result, expected)
	

	def test_createKeyTable(self):
		cipher = Cipher("Just another example", "Meet me at eight o clockSigned Agent Double O Eight")
		result = cipher.createKeyTable()
		expected = [['I', 'U', 'S', 'T', 'A'], ['N', 'O', 'H', 'E', 'R'], ['X', 'M', 'P', 'L', 'B'], ['C', 'D', 'F', 'G', 'K'], ['Q', 'V', 'W', 'Y', 'Z']]
		self.assertEqual(result, expected)



if __name__ == "__main__":
	unittest.main()