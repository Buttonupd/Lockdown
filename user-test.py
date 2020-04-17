import unittest
from user import User
from credentials import Credential


class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Set up method to run before each test case/s
        """
        self.new_user = User("Button", "Up", "0712345678", "button@mail.com")  # create user object

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        User.users_array = []

    def test_init(self):
        """
        test_init test case to test if object utilizes proper instantiation
        """
        self.assertEqual(self.new_user.first_name, "Button")
        self.assertEqual(self.new_user.last_name, "Up")
        self.assertEqual(self.new_user.phone_number, "0712345678")
        self.assertEqual(self.new_user.email, "button@mail.com")

    def test_save_user(self):
        """
         test case to test if the user object is saved in
         users array
        """
        self.new_user.save_user_details()  # saving the new user
        self.assertEqual(len(User.users_array), 1)

    def test_save_multiple_users(self):
        """

            this test-case method gives users the ability to save multiple account details
        """
        self.new_user.save_user_details()
        test_user = User("Test", "user", "0712345678", "test@user.com")  # new user
        test_user.save_user_details()
        self.assertEqual(len(User.users_array), 2)

    def test_log_in(self):
        '''
        Test case to test if a user can log into their credentials
        '''

        # Save the new user
        self.new_user.save_user_details()

        test_user = User("Button", "Up", "0712345678", "button@mail.com")

        test_user.save_user_details()

        found_credential = User.log_in("Button", "Up")

        self.assertEqual(found_credential, Credential.credential_list)

    def test_display_all_users(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(User.display_users(), User.users_array)


if __name__ == '__main__':
    unittest.main()
