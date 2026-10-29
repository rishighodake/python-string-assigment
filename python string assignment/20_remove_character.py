text = input("Enter a string: ")
character = input("Enter one character to remove: ")

if len(character) == 1:
    print("Updated string:", text.replace(character, ""))
else:
    print("Please enter exactly one character.")
