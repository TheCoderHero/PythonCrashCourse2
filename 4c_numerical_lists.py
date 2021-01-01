# Using the range() Function
for value in range(1, 5):
    print(value) # 1 2 3 4

for value in range(1, 6):
    print(value) # 1 2 3 4 5

# Using range() to Make a List of Numbers
numbers = list(range(1, 6))
print(numbers)

# Skipping Numbers in range() Function
# Third argument in range is what number to skip
even_numbers = list(range(2,11,2))
print(even_numbers)

# Making Square Numbers using range() Function
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) # 0
print(max(digits)) # 9
print(sum(digits)) # 45

# List Comprehensions
# Create the same squares list in a single line of code
comp_squares = [value ** 2 for value in range(1, 11)]
print(comp_squares)
# descriptive_name_of_list = [expression_for_the_values for values in range(range_of_numbers)]