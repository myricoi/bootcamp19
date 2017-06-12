import unittest
import prime
# returns a list
# returns a message for wrong input 
# returns correct list for small input
# returns correct list for large input
# Empty list if there are no primes
class Prime_test(unittest.TestCase):
	def test_returns_a_list(self):
		a=prime.gen_prime(0)
		self.assertTrue(isinstance(a,list),"The returned output should be a list")

	def test_returns_a_message_for_wrong_input(self):
		msg=prime.gen_prime([])
		self.assertEqual(msg,"Only an integer is allowed","The function should return a message telling user about wrong input")
	def test_returns_correct_ouput_for_small_values(self):
		n=prime.gen_prime(10)
		self.assertEqual(n,[2,3,5,7],"The return value is expected to be correct for input 10")

	def test_returns_correct_ouput_for_large_values(self):
		n=prime.gen_prime(100)
		self.assertEqual(n,[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97],"The return value is expected to be correct for input 100")

	def test_returns_empty_list_if_no_primes(self):
		n=prime.gen_prime(1)
		self.assertEqual(n,[],"The return value is expected to be correct if no primes are found")






if(__name__=='__main__'):
	unittest.main()