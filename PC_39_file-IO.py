# This is 39th code of this python Course
# this code demonstrates the use file handling in python

#Creating a file
with open("39_file2","w") as f:
        print(f.write("Hello...This is file 2"))


# Writing in the File
f=open("39_file","w")

paragraph = """Python is a powerful and beginner-friendly programming language.
It is widely used in web development, data science, automation, and more.
Learning Python opens the door to many exciting career opportunities.
Keep practicing, and you'll keep getting better every day!"""

f.write(f"Hello, I am wrinting in the file! \n"
        f"{paragraph}")
f.close()

# Reading the file
f=open("39_file",'r')
print(f.read())
f.close()




