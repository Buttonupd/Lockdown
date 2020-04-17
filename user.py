from credentials import Credential


class User:
    """
    this class generates new instances of users
    """
    pass

    users_array = []

    def __init__(self, first_name, last_name, phone_number, email, ):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_user_details(self):
        """
        save_contact method saves contact objects into user_array
        """
        User.users_array.append(self)

    @classmethod
    def log_in(cls, name, password):
        '''
        Method that allows a user to log into their credential
        Args:
            name : name of the user
            password : password for the user
        Returns:
            Credential list for the user that matches the name and password
            False: if the name or password is incorrect
        '''

        # Search for the user in the user list
        for user in cls.users_array:
            if user.first_name == name and user.last_name == password:
                return Credential.credential_list

        return False

    @classmethod
    def display_users(cls):
        """
        method that returns the class array
        """
        return cls.users_array
