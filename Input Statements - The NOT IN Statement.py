# Input Statements
# 10-18-2020
# The NOT IN Statement

membership_users = ['Bill', 'Bob']

username = input("Enter your username here:")

if username.title() not in membership_users:
    print("Sorry, you don't have a membership. Access Denied. ")
else:
    print("Congradulations! Access Granted.")