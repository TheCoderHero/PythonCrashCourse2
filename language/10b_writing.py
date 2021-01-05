# Basic write to file
filename = 'writefile.txt'

with open(filename, 'w') as file_object:
    file_object.write('Python Power!')

# Appending a file
with open(filename, 'a') as file_object:
    file_object.write("\nDon't forget the newline character or else your text will be smashed on one line.")
    file_object.write("\nAnd I mean for every new line. You miss one and you'll be in trouble.")