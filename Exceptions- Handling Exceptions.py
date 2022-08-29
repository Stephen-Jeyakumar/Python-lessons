# Exceptions
# 11-26-2020
# Handling exceptions

print("Enter 2 numbers to divide")
print(" Enter 'q' To quit the program.")

while True:
    first_number = input("\n First Number:")
    if first_number == 'q':
        break

    second_number = input("Second Number:")
    
    try:
        answer = float(first_number) / float(second_number)
    except ZeroDivisionError:
        print("ErRoR YoU CaNnOt DiViDe By zErO ErRoR eRrOr")
    except ValueError:
        print("ErRoR YoU CaNnOt DiViDe By LeTtErs ErRoR eRrOr")
    else:
        print(answer)
    
    


    if second_number == 'q':
        break


