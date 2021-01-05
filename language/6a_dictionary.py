# A Simple Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Accessing values in a dictionary
new_points = alien_0['points']

# Adding New Key-Value Pairs
alien_0['x-pos'] = 0
alien_0['y-pos'] = 25
print(alien_0)

# Starting with an empty dictionary
alien_1 = {}
alien_1['color'] = 'blue'
alien_1['points'] = 5
print(alien_1)

#Modifying values in a dictionary
alien_2 = {'color': 'green'}
alien_2['color'] = 'yellow'
print(alien_2)

# Practical Example
alien_master = {'x-pos' : 0, 'y-pos' : 25, 'speed' : 'medium',}
print(f"Original position: x:{alien_master['x-pos']} y:{alien_master['y-pos']}")

if alien_master['speed'] == 'slow':
    xPos = 1
elif alien_master['speed'] == 'medium':
    xPos = 2
else:
    xPos = 3

alien_master['x-pos'] = alien_master['x-pos'] + xPos

print(f"New position: x:{alien_master['x-pos']} y:{alien_master['y-pos']}")

#Removing ky-value pairs
print(alien_0)
del alien_0['points']
print(alien_0)

# Using get() method to access values in a dictionary
point_value = alien_master.get('points', 'No point value assigned this alien')
print(point_value)
# variable = dictionary.get(key, text if no key exists)
# If you leave the 2nd argument out of get(), it will return 'None'