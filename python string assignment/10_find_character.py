text = input("Enter a string: ")
character = input("Enter one character to find: ")

if len(character) == 1:
    print("Index:", text.find(character))
else:
    print("Please enter exactly one character.")
