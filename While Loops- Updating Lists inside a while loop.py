# While Loops
# 11-2-2020
# Updating Lists inside a While Loop

unconfirmed_users = ['Bob', 'bill', 'joe', 'fred']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print('\n The following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())