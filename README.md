Password Locker
    This is a Python application that allows a user to generate and store passwords for various accounts., 13/20/2017

Author
    By Dan Kariuki
Description
    This application lets users store various accounts information. The application runs on the terminal and the user navigates through the app by using predetermined short codes.

The short codes are:
    can - create a new_user account with a user_defined password\n

    cag- create a new auto-generated password

    lg - log into your Password Locker account

    cad - display all user accounts

    ex -exit the contact list

User Stories
    As a user I would like:

    To create an account with my details - log in and password
    Save my existing log_in credentials
    Generate a password for a new credential

Specifications
    _______Behavior	Input	Outcome_____________
    Create an account	User Name : Cringe_man
    Password : Mancringe	Creates an account
    Display account	N/A	Display a bunch of users credentials
    Log_in User Name : Cringe_man
    Password : Mancringe	Log into the users account
    Store existing log in credential	Account : Github
    Password : Cringer Create and save the user's credentials
    Display a specific users credentials	N/A	List of the user's credentials
    Generate a password for a new credential	Account : Password Locker	Generate a password for the user.
    Create and save the user's credential with the generated password
    Log out	N/A	Log out of Password Locker account

Prerequisites
    Python3.6 and above: System specification,python 3.7.4

Setup/Installation Requirements
    Clone this repository and run the run.py file.

Known Bugs
    No known bugs

Technologies Used
Python3.7.4
License
MIT (c) 2020 Dan Kariuki

