#!/usr/bin/env python3.7
from credentials import Credential
import datetime
from user import User
import random


def create_credential(fname, lname, password):
    new_credential = Credential(fname, lname, password)
    return new_credential


def create_user(fname, lname, phone, email):
    new_user = User(fname, lname, phone, email)
    return new_user


def save_credentials(credential):
    credential.save_credential()


def save_user(user):
    user.save_user_details()


def del_contact(credential):
    credential.delete_credential()


def del_user(user):
    user.delete_user()


def find_first_name(credential):
    return Credential.find_by_first_name(credential)


def check_existing_credentials(credential):
    return Credential.credential_exist(credential)


def display_credentials():
    return Credential.display_credentials()

def display_user():
    return User.display_users()


def main():
    print("Welcome to Locked-In. From the list of predetermined commands, choose one or more")
    while True:
        print("Basic Commands: \n can - create a new_user account with a user_defined password\n cag- create a new "
              "auto-generated password\n cad - display all user accounts \n ex -exit the contact "
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
            save_credentials(create_credential(f_name, l_name, password ))
            print("\n")
            print(f"A new {site} account by {f_name} successfully has been created")
            print(f"The user-name is {user_name} and the password is {password} ")
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
