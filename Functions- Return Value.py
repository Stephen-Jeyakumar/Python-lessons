# Functions
# 11-4-2020
# Return Value


def formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

teacher = formatted_name('diddy', 'kong')
print(teacher)

def get_formatted_username(email_address):
    username = email_address.strip()
    return username
user = get_formatted_username('example.example.com')
print(user)