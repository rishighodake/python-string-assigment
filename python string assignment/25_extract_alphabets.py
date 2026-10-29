text = input("Enter a string: ")
letters = ""

for character in text:
    if character.isalpha():
        letters += character

print("Alphabets:", letters)
