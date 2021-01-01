# Step 1 - Open Function - Filename as an argument
# 'with' keyword closes a file once it is finished being accessed
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

# File Paths - Relative (Relative to where the running program file is located)
with open('text_files/pi_digits_v2.txt') as file_object:
    contents = file_object.read()
print(contents)

# You can use absolute paths as well as relative paths

# Reading Line by Line
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Making a List of LInes from a File
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# Working with a File's Contents
pi_string = ""
for line in lines:
    pi_string += line.rstrip().lstrip()

print(pi_string)
print(len(pi_string))


# Does your birthday appear in the first 1 million digits of pie
millionpi = 'ResourceFiles/chapter_10/pi_million_digits.txt'
with open(millionpi) as file_object:
    lines = file_object.readlines()

mil_pi_string = ""

for line in lines:
    mil_pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in mil_pi_string:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday does not appear in the first million digits of pi')
