# This is the 15th code of this Python Course
# This code demonstrates the use of break and continue keywords

a = int(input("Enter a number : "))
for i in range(1, 21):
    print(a, "*", i, "=", a * i)
    if(i == 10):  # Stop the loop after 10 iterations
        break

a = int(input("Enter a number : "))
for i in range(1, 21):
    if(i == 5):  # Skip multiplication when i is 5
        print("Skip Iteration")
        continue
    print(a, "*", i, "=", a * i)
