# This is 30th code of this python course
# This code demonstrates the use of else in loop (i.e for-loop, while-loop)
from selectors import SelectSelector


for i in range(1,6):
    print(i)
else:
    print("This is else part of for-loop")


a=1
while a<5:
    print(f"count is {a}")
    a+=1
else:
    print("This is else part of while-loop")


for i in range(1,6):
    if i==3:
        break;
    print(i)
else:
    print("This is else part of for-loop")


a=1
while a<5:
    print(f"count is {a}")
    if a==3:
        break
    a+=1
else:
    print("This is else part of while-loop")