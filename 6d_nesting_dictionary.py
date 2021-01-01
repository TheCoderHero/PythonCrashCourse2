# A List of Dictionaries
alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'green', 'points' : 5}
alien_2 = {'color' : 'yellow', 'points' : 5}
alien_3 = {'color' : 'yellow', 'points' : 5}

aliens = [alien_0, alien_1, alien_2, alien_3]

for alien in aliens:
    print(alien)

# Practical Example (fleet of 30 aliens)
aliens = []
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('...')
print(f"Total aliens created = {len(aliens)}")

# A list in a dictionary
pizza = {
    'crust': 'thin',
    'toppings': ['mrm','pep','xch']
}
print(f"You ordered a {pizza['crust']} crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

# A dictionary in a dictionary
users = {
    'thein': {
        'username': 'tnguyen',
        'first' : 'thein',
        'last' : 'nguyen',
        'location' : 'River Road'
    },
    'douglas' : {
        'username': 'dfigueredo',
        'first' : 'douglas',
        'last' : 'figueredo',
        'location' : 'Venture'
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {user_info['username']}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"
    print(f"\tFull Name: {full_name}")
    print(f"\tLocation: {location}")
