class publisher:
    def publish(self):
        print("Publisher of the book")
class book(publisher):
    def title(self):
        print("Python")
    def author(self):
        print("Author of the book")
class python(book):
    def price(self):
        print("Price of the book is 400")
    def pages(self):
        print("Number of pages is 899")
obj1=python()
obj1.publish()
obj1.title()
obj1.author()
obj1.price()
obj1.pages()