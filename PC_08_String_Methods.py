# 8th code of this Python Course
# String functions in Python

s1 = "pavan"
print(s1.upper())                # Converts to uppercase → "PAVAN"

s2 = "DAMJI"
print(s2.lower())                # Converts to lowercase → "damji"

s3 = "Hello World"
print(s3.rsplit(" "))            # Splits from the right at space → ['Hello', 'World']

print(s3.replace("Hello", "Namaste"))  # Replaces "Hello" with "Namaste"

print(s3.split())                # Splits at spaces → ['Hello', 'World']

s4 = "this world is amazing"
print(s4.capitalize())          # Capitalizes first letter → "This world is amazing"

print(s3.center(30))            # Centers the string in 30-width space

print(s3.count("l"))            # Counts how many times "l" appears

print(s3.endswith("d"))         # Checks if string ends with 'd'

print(s3.find("e"))             # Finds index of first 'e'

print(s3.index("l"))            # Returns index of first 'l'

print("Pavan123".isalnum())     # True → only letters and numbers, no space or symbol

print("OnlyText".isalpha())     # True → all are alphabets

print("lowercase".islower())    # True → all lowercase

print("Hello\nWorld".isprintable())  # False → contains non-printable character \n

print("    ".isspace())         # True → only space characters

print("This Is Title Case".istitle())  # True → each word starts with capital

print("HELLO".isupper())        # True → all uppercase

print("Python is fun".startswith("Python"))  # True → starts with "Python"

print("PyTHon".swapcase())      # Swaps upper to lower and vice versa

print("hello world from python".title())  # Each word starts with capital letter
