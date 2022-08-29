# Input Statements 
# 10-18-2020
# The ELIF Statement 

balance = input("What is your bank balance?")
if int(balance) <= 0:
    print("Would you like to make a deposit?")
elif int(balance) <= 50:
    print("Sorry. You do not qualify for interest.")
elif int(balance) <100:
    print("Your interest rate is 1%.")
else:
    print("Your interest rate is 2%.")