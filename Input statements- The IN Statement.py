# Input statements
# 10-18-2020
# The IN Statement

avaiable_fruit = ['pineapple', 'orange', 'kiwi', 'dragonfruit']

username = input("Enter your fruit username here:")

if username in avaiable_fruit:
    print("Success! Fruit username Saved")
else: 
    print("Sorry, fruit username is taken")