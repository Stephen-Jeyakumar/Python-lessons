# Functions
# 11-3-2020
# How to Pass Information into a Function 
username = input("What is your username?")


def hello_world(username):
    print("Hello " + username.title() + ".")

hello_world(username)
