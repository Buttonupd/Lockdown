#!/usr/bin/env python3.7
from credentials import Credential
import datetime
from user import User
import random


def create_credential(fname, lname, password):
    """A functions which allows users to create new credentials"""
    new_credential = Credential(fname, lname, password)
    return new_credential


def create_user(fname, lname, phone, email):
    """This a function which gives users the ability to create new user accounts"""
    new_user = User(fname, lname, phone, email)
    return new_user


def save_credentials(credential):
    """This is a subsequent function which optimizes application performance by enhancing several different features
    as saving a variety of credentials and user details """
    credential.save_credential()


def save_user(user):
    """Almost similar to the class above, this saves user/s details"""
    user.save_user_details()


def del_contact(credential):
    """This class gives the application the ability to delete different user inputs or details"""
    credential.delete_credential()


def del_user(user):
    """This class gives the application the ability to delete different user inputs or details"""
    user.delete_user()


def user_log_in(name, password):
    """
    Function that allows a user to log into their credential account
    Args:
        name : the name the user used to create their user account
        password : the password the user used to create their user account
    """
    log_in = User.log_in(name, password)
    if log_in:
        return User.log_in(name, password)


def find_first_name(credential):
    """ A user can use this feature to locate account details by first_name if for some reason the rest is vague"""
    return Credential.find_by_first_name(credential)


def check_existing_credentials(credential):
    """Another exciting class gives users the privilege to check whether certain accounts, names or other details
    exist """
    return Credential.credential_exist(credential)


def display_credentials():
    """Depending on existing credentials, a user can utilize this feature because it does display the number of
    credentials available """
    return Credential.display_credentials()


def display_user():
    """This class has the power to display users credentials"""
    return User.display_users()


def main():
    print("Welcome to Locked-In. From the list of predetermined commands, choose one or more")
    while True:
        print("Basic Commands: \n can - create a new_user account with a user_defined password\n cag- create a new "
              "auto-generated password\n  lg - log into your Password Locker account \n cad - display all user "
              "accounts \n ex -exit the contact "
              "list \n")
        short_code = input().lower()

        if short_code == 'can':
            print("New user")
            print("-" * 10)
            print(" Hello! What account would you like to create credentials for? ")
            site = input()
            print("->->->->")

            print("First name ....")
            f_name = input()

            print("Last name")
            l_name = input()

            print("Phone Number")
            p_number = input()

            print("Email address")
            e_address = input()

            print("Enter username ...")
            user_name = input()

            print("Enter password")
            password = input()

            save_user(create_user(f_name, l_name, p_number, e_address))
            save_credentials(create_credential(f_name, l_name, password))
            print("\n")
            print(f"A new {site} account by {f_name} successfully has been created")
            print(f"The user-name is {user_name} and the password is {password} ")
            print("\n")

        elif short_code == 'lg':
            '''
            Logs in the user into their Password Locker account
            '''
            print("\n")
            print("Log into Password Locker Account")
            print("Enter the user name")
            user_name = input()

            print("Enter the password")
            user_password = input()

            if user_log_in(user_name, user_password) is None:
                print("\n")
                print("Please try again or create an account")
                print("\n")

        elif short_code == "cag":
            print("New user")
            print("-" * 10)
            print("Hello! Which account would you like to create credentials for ?  ")
            site = input()
            print("->->->->")

            print("First name ....")
            f_name = input()

            print("Lat name .....")
            l_name = input()

            print("Phone Number.....")
            p_number = input()

            print("Email Address")
            e_address = input()

            print("Enter username ... System will generate a secure password")
            user_name = input()

            p_generator = "12345678910!@#$%^&*()+-?><abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            password = "".join(random.sample(p_generator, 8))
            save_user(create_user(f_name, l_name, e_address, p_number))
            save_credentials(create_credential(f_name, l_name, password))
            print("\n")
            print(f"the username is {user_name} and the password is {password}")
            print("\n")

        elif short_code == "cad":
            if display_user():
                print("Here is a list of all your user accounts")
                print("\n")

                for user in display_user():
                    print(f"{user.first_name} {user.last_name} has credentials for this {site}")
                print("\n")
            else:
                print("\n")
                print("It looks like no account credentials exist at the moment. Consider creating one or more ")
                print("\n")
        elif short_code == "ex":
            print("Bye ...")
            break
        else:
            print("Invalid command")


if __name__ == '__main__':
    main()

#     print(" Hello, welcome to your credential list. What is your name? ")
#     user_name = input()
#     print(f"Hello {user_name}. What would you like to do")
#     print('\n')
#
#     while True:
#         print("Use these short codes : cc - create a new credential, dc - display  credentials, fc - find a "
#               "credential, ex - exit credential list ")
#         short_code = input().lower()
#         if short_code == 'cc':
#             print("New credential")
#             print("-" * 10)
#
#             print("First name ")
#             f_name = input()
#
#             print("Last name ...")
#             l_name = input()
#
#             print("password ...")
#             password = input()
#
#             save_credentials(create_credential(f_name, l_name, password))
#             print('/n')
#
#             print(f"New Credential {f_name} {l_name} created at", datetime)
#             print("\n")
#
#         elif short_code == 'dc':
#             if display_credentials():
#                 print("Here is a full list of your current credentials")
#                 print("\n")
#                 for credential in display_credentials():
#                     print(f"{credential.first_name}  {credential.last_name}  .....{credential.password}")
#                     print("\n")
#                 else:
#                     print("You don't seem to have any credentials yet")
#                     print("\n")
#
#             elif short_code == 'fc':
#                 print("Enter the password yo wont to look for")
#                 search_password = input()
#                 if check_existing_credentials(search_password):
#                     search_credential = find_first_name(search_password)
#                     print(f"{search_credential.first_name} {search_credential.last_name}")
#                     print('-' * 20)
#                     print(f"password ...... {search_credential.password}")
#                 else:
#                     print("That credential does not exist")
#
#             elif short_code == "ex":
#                 print("Bye .....")
#                 break
#             else:
#                 print("I really didn't get that. Please use the short codes")
#
#
# main()
