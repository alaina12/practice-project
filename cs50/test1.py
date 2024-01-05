import unittest
import script1

class TestGame(unittest.TestCase):
	def test_input(self):
		result = script1.run_guess(4,4)
		self.assertTrue(result)
	
	def test_input_wrong_guess(self):
		result = script1.run_guess(4,0)
		self.assertFalse(result)

	def test_input_wrong_number(self):
		result = script1.run_guess(4,11)
		self.assertFalse(result)

	def test_input_wrong_type(self):
		result = script1.run_guess(4,'5')
		self.assertFalse(result)
if __name__ == '__main__':
	unittest.main()		