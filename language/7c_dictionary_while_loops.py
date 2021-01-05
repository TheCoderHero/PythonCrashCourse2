# Moving items from one list to another
new_shipment = ['mush','pep','xch','gpep','pin']
received = []

while new_shipment:
    item = new_shipment.pop()
    print(f"Moving {item} to the fridge.")
    received.append(item)

print('The following items where received: ')
for item in received:
    print(f"\titem: {item}")

# Removing all instances of specific values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

# Filling a dictionary with user input
responses = {}
polling_active = True
while polling_active:
    name = input("Please enter your name: ")
    response = input("What is your favorite color? : ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? yes/no : ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} : {response}")