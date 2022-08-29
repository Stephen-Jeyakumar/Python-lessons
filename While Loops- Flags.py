# While Loops
# 10-30-2020
# Flags

prompt =  "\n Enter 'q' To quit this program"
prompt += "\n What is your name?"

active = True

while active:
    message = input(prompt)

    if message == 'q':
        active = False 
    else:
        print(message)
