# This is 32nd code of this python course
# This code demonstrates the use finally keyword

try:
    l=[1,2,3,4,5]
    print(l[6])
except Exception as e:
    print(e)
finally:
    print("This is finally block!")