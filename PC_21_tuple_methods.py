# This is 21st code of this python Course
# This code demonstrates the use of tuple methods


t = (1, 2, 3, 4, 2, 5, 2)

print(t.count(2))   # Output: 3 (2 appears 3 times)
print(t.index(4))   # Output: 3 (4 is at index 3)

t2 = (1, 3, 2)
l = list(t2)
l.append(4)
print(tuple(l))  # (1, 3, 2, 4)
