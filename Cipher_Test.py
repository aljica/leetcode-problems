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
		cipher = Cipher("hEllo world", "stop")
		cipher.createKeyTable()
		result = cipher.encrypt()
		expected = "TNES"

		self.assertEqual(result, expected)



if __name__ == "__main__":
	unittest.main()