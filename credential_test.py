import unittest
from credentials import Credential
import pyperclip


class TestCredential(unittest.TestCase):

    def setUp(self):

        # Credential.credential_list = []
        self.new_credential = Credential("Button", "up", "Dan")

    def test_init(self):
        self.assertEqual(self.new_credential.first_name, "Button")
        self.assertEqual(self.new_credential.last_name, "up")
        self.assertEqual(self.new_credential.password, "Dan")

    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def tearDown(self):

        Credential.credential_list = []

    def test_save_multiple_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential("Humans", "are", "Mortal")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_delete_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential("Humans", "are", "Mortal")
        test_credential.save_credential()
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_find_credential_by_first_name(self):
        self.new_credential.save_credential()
        test_credential = Credential("Mighty", "Diamonds", "Marcus")
        test_credential.save_credential()

        found_credential = Credential.find_by_first_name("Mighty")
        self.assertEqual(found_credential.password, test_credential.password)

    def test_credential_exists(self):

        self.new_credential.save_credential()
        test_credential = Credential("Mighty", "Diamonds", "Marcus" )
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("Marcus")
        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):

        self.assertEqual(Credential.display_credentials(), Credential.credential_list)

    def test_copy_first_name(self):
        self.new_credential.save_credential()
        Credential.copy_first_name("Marcus")
        self.assertEqual(self.new_credential.first_name, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
