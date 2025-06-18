# This is 53rd code of this python course
# This code is a mini project of Library Management System also using file management...
# !!!Yet some work remained...gonna complete soon
import sys


class library:


    def listofbooks(self):
        openfile = open("52_Library2-file", 'r')
        line = openfile.read()
        books = line.split(",")
        i=1
        for book in books:
            print(f"{i}. {book}")
            i+=1

    def addbook(self,bookname):
        self.bookname=bookname
        with open("52_Library2-file", 'a') as addbookfile :
            addbookfile.write(" ,"+bookname)
        print(f"The book {bookname} have been added successfully!")

    def borrowbook(self, bb):

        self.bb = bb.strip()
        with open("52_Library2-file", 'r') as borrowbookfile:
            data = borrowbookfile.read()
            names=[]
            for name in data.split(','):
                names.append(name.strip())
        if self.bb in names:
            names.remove(self.bb)
            with open("52_Library2-file", 'w') as updatelist:
                updatelist.write(", ".join(names))
            print(f"Book '{self.bb}' has been removed successfully!")
        else:
            print(f"Book '{self.bb}' does not exist!")

    def exitlibrary(self):
        sys.exit()


l = library()
while(True):
    print("********************* WELCOME TO LIBRARY *********************")
    print("1. Check list of books")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Exit")

    choice = int(input("Choose : "))

    match choice :
        case 1:
            print("_____________________________________________________")
            l.listofbooks()
            print("_____________________________________________________")

        case 2:
            print("_____________________________________________________")
            adb = input("Enter Book name to Add : ")
            l.addbook(adb)
            print("_____________________________________________________")

        case 3:
            print("_____________________________________________________")
            print("Available Books!")
            print("_____________________________________________________")
            l.listofbooks()
            reb = input("Enter Book name to remove : ")
            l.borrowbook(reb)
            print("_____________________________________________________")

        case 4:
            print("_____________________________________________________")
            print("Thanks for using!")
            print("Exiting........")
            exit()
