# input() function
username = input('Please enter your username:')
print(f"Hello, {username}")
password = input('Please enter your password:')
print("**********")

prompt = 'We need to gather some important information first.'
prompt += '\nPlease enter your first name: '
name = input(prompt)
print(f"Hello, {name}. I am pleased to meet you.")

# Int for inputing integers
age = input(f"{name}, please enter your age: ")
age = int(age)
if age > 18:
    print(f'Awesome! {name}, you are old enough to vote!')
else:
    print(f"Sorry, {name}, you are not old enough to vote yet.")