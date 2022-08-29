# Numerical Lists
# 10-13-2020
# Making a list of numbers/ exploring Lists with numbers

numbers = list(range(1,6))
print(numbers)

odd_numbers = list(range(1, 101, 2))
print(odd_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = [1,2,3,4,5]
print(min(digits))
print(max(digits))
print(sum(digits))