from user import User


def login():
    user = input("Enter username")
    password = input("Enter password")
    if user == user.join(User.first_name):
        print("did")


login()

# import csv
#
#
# def chain():
#     with open("user.py") as file:
#         file_reader = csv.reader(file)
#         user_find(file_reader)
#         file.close()
#
#
# def user_find(file):
#     user = input("Enter your username")
#     for row in file:
#         if row[0] == user:
#             print("Username found", user)
#             user_found = [row[0], row[1]]
#             pass_check(user_found)
#             break
#         else:
#             print("not found")
#
#
# def pass_check(user_found):
#     user = input("Enter your password")
#     if user_found[1] == user:
#         print("password match")
#     else:
#         print("password failed")
#
#
# chain()
