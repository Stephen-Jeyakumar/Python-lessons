# While Loops
# 10-31-2020
# The CONTINUE Statement

current_number = 0

while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        continue 

print(current_number)
