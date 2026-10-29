text = input("Enter a string: ")
character = input("Enter one character to find: ")

if len(character) == 1:
    print("First occurrence:", text.find(character))
    print("Last occurrence:", text.rfind(character))
else:
    print("Please enter exactly one character.")
