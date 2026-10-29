text = input("Enter a string: ")
reversed_text = ""

for character in text:
    reversed_text = character + reversed_text

print("Is palindrome:", text == reversed_text)
