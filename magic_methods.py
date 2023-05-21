class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self):
        return int(self.pages)

    def __str__(self):
        return "The {} is written by {}".format(self.title, self.author)

    def normal_method(self):
        return "This is the normal method"

booktitle = input("Pls enter the book title :")
bookauthor = input("Pls enter the author of the book :")
bookpages = input("Pls enter the no. of pages in the book :")

b = Book(booktitle, bookauthor, bookpages)

print(len(b))

print(str(b))

print(b.normal_method())
