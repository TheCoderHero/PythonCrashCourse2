user_0 = {
    'username' : 'The Coder Hero',
    'full_name' : 'The Coder Hero',
    'first' : 'The Coder',
    'last' : 'Hero',
}

# For loop
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# for 'name of key', 'name of value' in 'name of dictionary'.items()

# Looping through the keys
for key in user_0.keys():
    print(key.title())
# This is the default action so: 'for key in user_0:' would work the same

# keys method to see if exists in the dictionary
if 'password' not in user_0.keys():
    print(f"{user_0['username'].title()} has not provided a password")

# Sorting keys in a dictionary
for keys in sorted(user_0.keys()):
    print(f"{keys}")\

# Looping through the values
for values in user_0.values():
    print(f"{values}")

# set() removes duplicate values
for values in set(user_0.values()):
    print(f"{values}")