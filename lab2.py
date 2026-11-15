class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Book Title: {self.title}, Author: {self.author}")


book1 = Book("sindhi", "Ali ")
book2 = Book("English", "Asghar")
book3 = Book("Artificial Intelligence", "Alan Turing")

book1.display_info()
book2.display_info()
book3.display_info()