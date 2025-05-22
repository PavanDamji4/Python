# 5th code of this Python Course
# Type Casting

# -------- Explicit Type Casting --------

a = "2"
b = "3"
print(a + b)            # Both are strings → result is string concatenation → "23"

a = "2"
b = "3"
print(int(a) + int(b))  # Strings converted to int → added as numbers

a = "2"
b = 3
print(a + str(b))       # int b converted to string → then concatenated

# -------- Implicit Type Casting --------

a = 5
b = 2.5
c = a * b
print(c)                # int and float → result is float

x = 10
y = 3.0
z = x + y
print(z)                # int + float → result is float
