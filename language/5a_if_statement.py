colors = ['black', 'blue', 'yellow', 'red', 'green', 'purple']
for color in colors:
    if color == 'black':
        print(color.upper())
    else:
        print(color.title())

# Conditional Statement (TRUE or FALSE)

# Checking for equality ==
number = 0
print(number == 1) # False

# Checking for equality IS cAsE sEnSiTiVe
green = 'GReen'
print(green == 'GREEN') # False
print(green.upper() == 'GREEN') # True

# Checking for inequality !=
requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print('Hold the Anchovies!')

# Numerical Comparisons
age = 21
print(age == 21) # True
print(age > 20) # True
print(age < 20) # False
print(age != 21) # False
print(age >= 21) #True
print(age <= 20) # False

# Checking Multiple Conditions 'and'
print(age > 20 and age < 25) # True
print(age > 25 and age < 20) # False

# Checking if a value is in a list 'in'
print('black' in colors) # True
print('beige' in colors) # False

# Checking if a value is not in a list
bad_color = 'house'
if bad_color not in colors:
    print(f"{bad_color.title()}, is not a good color!")

# Boolean Expressions
game_active = True
can_edit = False
