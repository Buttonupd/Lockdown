import unittest
from credentials import Credential


class TestCredential(unittest.TestCase):

    def setUp(self):
        self.new_credential = Credential("Button", "up", "Dan")

    def test_init(self):
        self.assertEqual(self.new_credential.first_name, "Button")
        self.assertEqual(self.new_credential.last_name, "up")
        self.assertEqual(self.new_credential.password, "Dan")

    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_save_multiple_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential("Humans", "are", "Mortal")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)


if __name__ == '__main__':
    unittest.main()
