import unittest  # Importing the unittest module

from user import User  # Importing the contact class


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours
    """

    def setUp(self):
        """
        set up method to run before each test cases.

        """

        self.new_user = User("shem", "kariuki", "shem@gmail.com", "1234")  # create user object

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly

        """

        self.assertEqual(self.new_user.first_name, "shem")
        self.assertEqual(self.new_user.last_name, "kariuki")
        self.assertEqual(self.new_user.email, "shem@gmail.com")
        self.assertEqual(self.new_user.login_password, "1234")

    def test_save_user(self):
        """
        test_save_user test cas to test if the user object is saved into te user_list

        """

        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        User.user_list = []

    def test_save_multiple_users(self):
        """"
        test_save_multiple_users to check if we can save multiple user objects to our user_list
        """
        self.new_user.save_user()
        test_user = User("test", "user", "test@gmail.com", "5678")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)


if __name__ == '__main__':
    unittest.main()
