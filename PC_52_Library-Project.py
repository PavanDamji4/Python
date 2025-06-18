# This is 52nd code of this python course
# This code is a mini project of Library Management System...

class Library:
    books = ["To kill mocking bird", "Matilda"]
    no_of_books=2


    def listofbooks(self):
        srno = 1
        for i in self.books:
            print(srno,i)
            srno+=1

    def addbook(self,new_book):
        self.books.append(new_book)
        print("Book Added Successfully! ")

    def removebook(self,remove_book):
        try:
            self.books.remove(remove_book)
            print("Book Removed Successfully!")
        except Exception as e:
            print(f"Error**\nThe {remove_book} does not exist!")


l = Library()





