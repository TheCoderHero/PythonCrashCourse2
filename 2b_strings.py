# Strings
string_single_quote = 'String wrapped in single quotes'
string_double_quote = "String wrapped in double quotes"

# Changing Case in a String with Methods
name = 'the coder hero'
print(name.title()) # The Coder Hero
print(name.upper()) # THE CODER HERO
print(name.lower()) # the coder hero

# Using Variables in Strings
# f = format to string aka f-string
first_name = 'the coder'
last_name = 'hero'
full_name = f"{first_name} {last_name}"
print(full_name) # the coder hero

print(f"Hello, {full_name.title()}!") # Hello, The Coder Hero!
message = f"Hello, {full_name.title()}!"
print(message) # Hello, The Coder Hero!

# Adding Whitespace to Strings with Tabs or Newlines
# tab = \t
print('Python')   # Python
print("\tPython") #         Python
# newline = \n
print('Languages:\nPython\nC++\nHTML\nCSS\nJavascript')
# newline + tabs
print('Languages:\n\tPython\n\tC++\n\tHTML\n\tCSS\n\tJavascript')

# Stripping whitespace
# Right Side = rstrip()
# Left Side  = lstrip()
favorite_language = "Python    "
print(favorite_language)
favorite_language = favorite_language.rstrip()
favorite_language = favorite_language.lstrip()
print(favorite_language)