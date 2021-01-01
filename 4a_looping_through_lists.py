# Looping Through an Entire List
magicians = ['alice', 'david', 'merlin', 'gandalf', 'archemedis']
for magician in magicians:
    print(magician)

# Doing More Work Within a FOR Loop
for magician in magicians:
    print(f"{magician.title()}, performed an amazing trick!")
    print(f"Please perform another feat of magic, {magician.title()}\n")

# Doing Something After a FOR Loop
for magician in magicians:
    print(magician)
print('That is all the magicians I know!')