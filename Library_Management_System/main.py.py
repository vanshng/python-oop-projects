class Book():
    def __init__(self,title,author,available):
        self.title = title
        self.author = author
        self.available = available

    def display_book(self):
        print(f" Title : {self.title} \n Author : {self.author} \n Available : {self.available}")
    

class Library():
    def __init__(self):
      self.books = []
      
    def add_book(self,book):
        self.books.append(book)
        print(f'{book.title} added successfully!' )

    def show_books(self):
        if len(self.books) == 0:
            print('No books available in the library.')
        else :
            print('\n=====Library Books=====')
            for book in self.books:
                book.display_book()
        


book1 = Book('Pyhton Basics','Amer Nath','Yes')
book2 = Book("Data Structures", "John Smith", "Yes")
book3 = Book("Machine Learning", "Andrew Ng", "No")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.show_books()

