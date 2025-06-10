# This is 40th code of this python course
# This code demonstrates the use of various file methods such as seek(), tell(), truncate()

with open("40_file",'w') as f:
    f.write("I am a good boy")
    f.close()

f2=open("40_file",'r')
f2.seek(5)  # This method starts reading file from 5th index
print(f2.tell())
print(f2.read())
f2.close()

f2 = open("40_file", 'w')  # or use 'w+' if you want to overwrite the file
f2.truncate(5)              # truncate works only in write mode
f2.seek(0)
print(f2.write("This World is amazing"))
f2.close()