# Function(arg1, arg2)
# CallToFunction(arg1, arg2) -> Positional Arguments

# Function(arg1, arg2)
# CallTo Function(arg2='info', arg1='info') -> Keyword Arguments

# Function(arg1='info') -> Default Value

# Sending a copy of a list to a function
# functionCall(listName[:])

# Sending an arbitrary(dynamic) amount of arguments to a function
def make_pizza(*toppings):
    print(toppings)

make_pizza('much', 'pep')
make_pizza('xch', 'pep', 'gpep', 'olv')

# Positional and Arbitrary arguments
# Positional arguments must come first, then arbitrary arguments are last
def make_best_pizza(size, *toppings):
    print(f"Making a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"\t{topping}")

make_best_pizza('large', 'gpep', 'pep', 'mush', 'xch')

# Using arbitrary keyword Arguments
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstien', location='princeton', field='physics', hair='crazy')
print(user_profile)