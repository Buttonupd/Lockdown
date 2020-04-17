import unittest
from credentials import Credential
import pyperclip


class TestCredential(unittest.TestCase):

    def setUp(self):
        """setUp method run before most test case/s"""

        # Credential.credential_list = []
        self.new_credential = Credential("Button", "up", "Dan")

    def test_init(self):
        self.assertEqual(self.new_credential.first_name, "Button")
        self.assertEqual(self.new_credential.last_name, "up")
        self.assertEqual(self.new_credential.password, "Dan")

    def test_save_credential(self):
        """test_save_credential ensures that save credentials works properly"""
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def tearDown(self):
        """tearDown method allows it to be the case that clean up exercises on apps can be done without too much
        friction """

        Credential.credential_list = []

    def test_save_multiple_credential(self):
        """This test_save_multiple_credential allows devs to check whether saving multiple credentials is a smooth
        run not to inhibit users who may have such a need """
        self.new_credential.save_credential()
        test_credential = Credential("Humans", "are", "Mortal")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_delete_credential(self):
        """This method, a test case allows to check for deletions which the user might inject"""
        self.new_credential.save_credential()
        test_credential = Credential("Humans", "are", "Mortal")
        test_credential.save_credential()
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_find_credential_by_first_name(self):
        """This test_case allows the possibility of locating a credential while only using a name"""
        self.new_credential.save_credential()
        test_credential = Credential("Mighty", "Diamonds", "Marcus")
        test_credential.save_credential()

        found_credential = Credential.find_by_first_name("Mighty")
        self.assertEqual(found_credential.password, test_credential.password)

    def test_credential_exists(self):

        """this is to check whether there are existing credentials in a users account"""

        self.new_credential.save_credential()
        test_credential = Credential("Mighty", "Diamonds", "Marcus" )
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("Marcus")
        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):
        """This test_case feature is responsible for displaying available account credentials"""
        self.assertEqual(Credential.display_credentials(), Credential.credential_list)

    # def test_copy_last_name(self):
    #     self.new_credential.save_credential()
    #     Credential.copy_last_name("Diamonds")
    #     self.assertEqual(self.new_credential.last_name, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()

