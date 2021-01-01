# What is a List?
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List
print(bicycles[0]) # trek
print(bicycles[0].title()) # Trek

# Index Positions Start at 0, Not 1

# Access last element
print(bicycles[-1]) # specialized

# Using Individual Values from a List

message = f"My first bicycle was a {bicycles[0].title()}."
print(message) # My first bicycle was a Trek.

# Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati'
print(motorcycles) # ['ducati', 'yamaha', 'suzuki']

# Appending (adding) Elements to the End of a List
motorcycles.append('honda')
print(motorcycles) # ['ducati', 'yamaha', 'suzuki', 'honda']

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles) # ['honda', 'yamaha', 'suzuki']

# Insterting Elements into a List
motorcycles.insert(0, 'ducati')
print(motorcycles) # ['ducati', 'honda', 'yamaha', 'suzuki']

# Removing Elements from a List
del motorcycles[0]
print(motorcycles) # ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles) # ['yamaha', 'suzuki']


# Removing an Item Using the pop() Method
# pop() allows you to remove an item but still use its value

popped_motorcycle = motorcycles.pop()
print(motorcycles) # [yamaha']
print(popped_motorcycle) # suzuki

# Popping Items from any Position in a List
colors = ['red', 'blue', 'green', 'yellow', 'black', 'purple']
favorite_color = colors.pop(4)
print(f"My favorite color is {favorite_color.title()}.") # My favorite color is Black.

# Removing an Item by Value
colors.remove('yellow')
print(colors)