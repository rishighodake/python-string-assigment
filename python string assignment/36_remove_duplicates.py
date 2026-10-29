text = input("Enter a string: ")
result = ""

for character in text:
    if character not in result:
        result += character

print("Without duplicate characters:", result)
