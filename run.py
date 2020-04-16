#!/usr/bin/env python3.7
from credentials import Credential
import datetime


def create_credential(fname, lname, password):
    new_credential = Credential(fname, lname, password)
    return new_credential


def save_credentials(credential):
    credential.save_credential()


def del_contact(credential):
    credential.delete_credential()


def find_first_name(credential):
    return Credential.find_by_first_name(credential)


def check_existing_credentials(credential):
    return Credential.credential_exist(credential)


def display_credentials():
    return Credential.display_credentials()


def main():
    print(" Hello, welcome to your credential list. What is your name? ")
    user_name = input()
    print(f"Hello {user_name}. What would you like to do")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new credential, dc - display  credentials, fc - find a "
              "credential, ex - exit credential list ")
        short_code = input().lower()
        if short_code == 'cc':
            print("New credential")
            print("-" * 10)

            print("First name ")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("password ...")
            password = input()

            save_credentials(create_credential(f_name, l_name, password))
            print('/n')

            print(f"New Credential {f_name} {l_name} created at", datetime)
            print("\n")

        elif short_code == 'dc':
            if display_credentials():
                print("Here is a full list of your current credentials")
                print("\n")
                for credential in display_credentials():
                    print(f"{credential.first_name}  {credential.last_name}  .....{credential.password}")
                    print("\n")
                else:
                    print("You don't seem to have any credentials yet")
                    print("\n")

            elif short_code == 'fc':
                print("Enter the password yo wont to look for")
                search_password = input()
                if check_existing_credentials(search_password):
                    search_credential = find_first_name(search_password)
                    print(f"{search_credential.first_name} {search_credential.last_name}")
                    print('-' * 20)
                    print(f"password ...... {search_credential.password}")
                else:
                    print("That credential does not exist")

            elif short_code == "ex":
                print("Bye .....")
                break
            else:
                print("I really didn't get that. Please use the short codes")



