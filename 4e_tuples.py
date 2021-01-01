# CONSTANT = value that does not change
# TUPLE = list of values that don't change

# Creating a tuple
known_dimensions = (0, 1, 2, 3)
print('Here is a list of deminsions we know about:')
for dimension in known_dimensions:
    print(dimension)

# Because tuples do not change, we can not add, subtract, or modify this list
# #ERROR# # known_dimensions.append(4)
# #ERROR# # known_dimensions[0] = 4
print(known_dimensions)

# Writing over a tuple
known_dimensions = (0, 1, 2, 3, 4)
print(known_dimensions)