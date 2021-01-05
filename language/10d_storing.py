# Store data in JSON format
# JSON.DUMP()
# JSON.LOAD()

import json

# JSON.dump is a json write method
numbers = [2,4,6,8,10]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)



filename = 'username.json'
try:
    with open(filename) as f:
        #json.load is a json read method
        username = json.load(f)
except FileNotFoundError:
    username = input("Please enter your name: ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember your name when you come back {username}")
else:
    print(f"Welcome Back, {username}!")