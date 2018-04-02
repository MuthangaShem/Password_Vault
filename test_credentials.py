import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):

    """
    test class that defines test cases for the credential class behaviours
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        '''
        set up method to run before each test case
        '''
        self.new_credentials = Credentials("gmail", "kariukishem", "098765") # create credentials object
        

