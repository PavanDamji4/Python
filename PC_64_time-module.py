# This is 64th code of this python course
# This code demonstrates the use of time module

import time
from time import localtime

print(localtime())
formatted_time = time.strftime('%d/%m/%Y %H:%M:%S')
print(formatted_time)

print("Hello")
time.sleep(5)
print("This is being printed after 5 sec")

i=0
while i<50:
    print(i)
    i+=1

init=time.time()
print(time.time()-init)