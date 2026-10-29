text = input("Enter a string: ")
digits = ""

for character in text:
    if character.isdigit():
        digits += character

print("Digits:", digits)
