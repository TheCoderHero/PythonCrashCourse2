# if conditional_test:
    # do something

age = 19
if age >= 18:
    print('You are old enough to vote!') # This line prints
    # You can have multiple lines of code in an if statement
    print('Have you registered to vote yet?') # This line prints

# if-else Statements
new_age = 17
if new_age >= 18:
    print('You have reached adulthood!')
else:
    print('Sorry, you are still just a kid!') # This line prints

# if-elif-else Chain

child = 12
if child < 1:
    print('This is a baby')
elif child > 1 and child <= 5:
    print('This is a toddler')
elif child >= 5 and child <= 12:
    print('This is a small child')
elif child >= 13 and child <= 17:
    print('This is a teenager')
else:
    print('This is an adult')

# Sometimes it's better to use multiple if statements
toppings = ['mushrooms', 'extra cheese']
if 'pepperoni' in toppings:
    print('Adding pepperoni')
if 'mushrooms' in toppings:
    print('Adding mushrooms')
if 'extra cheese' in toppings:
    print('Adding extra cheese')
print('\nWe are busy making your pizza!')
 