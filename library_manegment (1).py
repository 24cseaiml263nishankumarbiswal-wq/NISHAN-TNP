class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Added: '{title}' by {author}")

    def show_books(self):
        for i, book in enumerate(self.books):
            status = "Available" if book.is_available else "Checked Out"
            print(f"{i+1}. {book.title} - {status}")

    def borrow_book(self, index):
        if 0 <= index < len(self.books):
            if self.books[index].is_available:
                self.books[index].is_available = False
                print(f"Success! You borrowed '{self.books[index].title}'.")
            else:
                print("Sorry, that book is already checked out.")
        else:
            print("Invalid book number.")
my_library = Library()
my_library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
my_library.add_index = my_library.add_book("1984", "George Orwell")
my_library.show_books()
my_library.borrow_book(0) 
my_library.show_books()