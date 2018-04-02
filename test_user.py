import unittest
from contact import Contact

class TestContact(unittest.TestCase):
	""Test class that defines test cases for the contact class behaviours."""
	def __init__(self, arg):
		super(TestContact, self).__init__()
		self.arg = arg
		