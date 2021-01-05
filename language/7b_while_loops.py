# Basic While Loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Practical Example
prompt = "\nEnter Phrase"
prompt += "\nEnter 'quit' to exit program: "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# FLAGS
active = True # This is the conditional flag
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    
    else:
        print(message)

# BREAK - Exit while loop immediately
# CONTINUE - Return to start of the loop (break out of current loop iteration)