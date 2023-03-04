from utils import cmd_at, xquic_command, generate_random_paths_num

import unittest

class TestCmdAt(unittest.TestCase):
	def test_xquic_command(self):
		pass
		# cmd_at("h", xquic_command, ifbackend=False, type="client", XQUIC_PATH="./")
		# self.assertEqual(sum([1,2,3]), 6, "Should be 6")


class TestUtil(unittest.TestCase):
	def test_generate_random_paths_num(self):
		print(generate_random_paths_num(1,10))
		print(generate_random_paths_num(1,10))
		print(generate_random_paths_num(1,10))
		

if __name__=="__main__":
  unittest.main()