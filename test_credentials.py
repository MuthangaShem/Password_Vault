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
        self.new_credentials = Credentials(
            "gmail", "kariukishem", "098765")  # create credentials object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.website, "gmail")
        self.assertEqual(self.new_credentials.username, "kariukishem")
        self.assertEqual(self.new_credentials.password, "098765")


if __name__ == '__main__':
    unittest.main()
