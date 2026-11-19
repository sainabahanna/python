class Publisher:
    def __init__(self):
        self.pid = input("publisher id: ")
        self.name = input("publisher name: ")


class Book(Publisher):
    def __init__(self):
        super().__init__()
        self.title = input("title: ")
        self.author = input("author: ")


class Python(Book):
    def __init__(self):
        super().__init__()
        self.price = input("price: ")
        self.pages = input("pages: ")

    def display(self):
        print(self.pid, self.name, self.title, self.author, self.price, self.pages)


x = Python()
x.display()
