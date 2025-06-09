# This is 37th code of this python course
# This code demonstrates the use of os modules and there function

import os

# os.mkdir("PC_37_Data")
#
# for i in range(1,11):
#     os.mkdir(f"PC_37_Data/File {i}")
#     os.rename(f"PC_37_Data/File {i}",f"PC_37_Data/Folder {i}")

folders = os.listdir("PC_37_Data")

for f in folders:
    print(os.listdir(f"PC_37_Data/{f}"))

