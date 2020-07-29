class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return "The {} is written by {}".format(self.title, self.author)

    def normal_method(self):
        return "This is the normal method"


b = Book("harry Potter", "J K Rowlings", 800)
print(len(b))
print(str(b))
print(b.normal_method())
