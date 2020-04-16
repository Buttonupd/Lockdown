import unittest
from credentials import Credential


class TestCredential(unittest.TestCase):

    def setUp(self):
        self.new_credential = Credential("Button", "up", "Dan")
