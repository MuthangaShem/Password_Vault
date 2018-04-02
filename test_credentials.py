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

    def test_save_credentials(self):
        '''
        test_save_contact test case to test if the credentials object is saved into
         the credential list
        '''
        self.new_credentials.save_credentials()  # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credential
        objects to our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "facebook", "karis mesh", "paswad")  # new credentials
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)


if __name__ == '__main__':
    unittest.main()
