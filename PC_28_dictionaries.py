# This is 28th code of this python course
# This code demonstrates the use of dictionaries in Python

d = {101:"Rohan",102:"Soham",103:"Saurabh",104:"Ishwar",105:"Pavan"}

print(d)

print(d.keys())
print(d.values())

print(d[103])

for values in d:
    print(values)

for key in d.keys():
    print(f"The student of roll number {key} is {(d[key])}")
