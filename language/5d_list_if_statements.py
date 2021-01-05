# Simple for loop
toppings = ['mushrooms', 'pepperoni', 'extra cheese']

for topping in toppings:
    print(f"Adding {topping.title()}")
print("\nPizza is going into the oven")

# Add a topping
toppings.append('green peppers')

# Check element for conditional statement in list
for topping in toppings:
    if topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print(f"Adding {topping.title()}")
print("\nPizza is going into the oven")

# Checking that a list is not empty
pizza = []
if pizza:
    for topping in pizza:
        print(f"Adding {topping.title()}")
    print('\nWorking on your pizza now!')
else:
    print('Are you sure oyu want a blank pizza')

# Using multiple lists
av_toppings = ['pep', 'grp', 'msh', 'xch']
rq_toppings = ['french fries', 'pep', 'xch']

for topping in rq_toppings:
    if topping in av_toppings:
        print(f"Adding {topping.title()} to pizza!")
    else:
        print(f"Sorry, we don't have {topping} available at this time.")
print('Pizza is going into the oven!')