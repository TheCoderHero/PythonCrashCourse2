# Exceptions are error objects that stop the program and notifies you of an error
# print(5/0) -> ZeroDivisionError: division by zero

# try-except block
try:
    print(5/0)
except ZeroDivisionError:
    print("Can not divide a number by zero!")

print("Enter 2 numbers to show division answer.")
print("Enter 'q' to quit.")
# Error Prone Code - No Exception Handling
# while True:
#     first_number = input("\nFirst Number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond Number: ")
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond Number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can not divide by 0!")
    else:
        print(answer)

# FileNotFoundError
filename = 'alice.txt'
try:
    with open(filename, encoding='utf8') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

# To simply run the program without informing the user of any issues use the 'pass' keyword