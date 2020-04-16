import pyperclip


class Credential:
    credential_list = []

    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_credential(self):

        Credential.credential_list.append(self)

    def delete_credential(self):

        Credential.credential_list.remove(self)

    @classmethod
    def find_by_first_name(cls, first_name):
        for credential in cls.credential_list:
            if credential.first_name == first_name:
                return credential

    @classmethod
    def credential_exist(cls, password):
        for credential in cls.credential_list:
            if credential.password == password:
                return True

    @classmethod
    def display_credentials(cls):
        return cls.credential_list

    @classmethod
    def copy_first_name(cls, first_name):
        credential_found = Credential.find_by_first_name(first_name)
        pyperclip.copy(credential_found.first_name)
