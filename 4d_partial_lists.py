# Slicing a List
colors = ['black', 'blue', 'green', 'yellow', 'red', 'purple']

# From start to another element
# colors 0, 1, 2
print(colors[0:3])

# From an element to another element
# colors 2, 3, 4
print(colors[2:5])

# From beginning of list to another element
# colors 0, 1, 2, 3
print(colors[:4])

# From an element of the list to the end
# colors 2, 3, 4, 5, 6
print(colors[2:])

# From -3 elements from the end to the end
# colors 4, 5, 6
print(colors[-3:])

# Looping Through a Slice
print("My families favorite colors are:")
for color in colors[:3] :
    print(f"\t{color.title()}")

# Copying a List
family_colors = colors[:3]
print(f"{family_colors}")

# The following does not copy a list
other_colors = family_colors
# This sets the value of other_colors to the value of family_colors (reference)