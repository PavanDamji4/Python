# This is 31st code of this python course
# This code demonstrates the use of Exception Handling

try:
    l = [1,2,3,4,5]
    print(l[6])
except Exception as e:
    print(e)

try:
    a = int(input("Enter a number : "))
    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")

except :
    print("Invalid input")