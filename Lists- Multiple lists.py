# Lists
# 10-20-2020
# Multiple Lists

Shopping_Cart = ['banana', 'ice cream', 'dog-food']

In_Stock = ['banana', 'ice cream']

for item in Shopping_Cart:
    if item in In_Stock:
        print("Adding " + item + " to your order.")
    else:
        print("Sorry, " + item + " is not in stock.")
print("Your order is complete.")