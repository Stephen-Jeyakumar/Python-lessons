# Input Statements
# 10-17-2020
# The OR statement

your_age = input("How old are you?")
friends_age = input("How old is your friend?")

if int(your_age) >= 18 or int(friends_age) >= 18:
    print("Congrats! One of you is old enough to vote!")
else: 
    print("Sorry, One of you isn't old enough to vote.")
