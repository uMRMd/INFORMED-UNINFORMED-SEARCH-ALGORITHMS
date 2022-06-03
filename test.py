class Bookstore:
    def __init__(self, book_list, quantity_list, price_list):
        self.book_dict = {}
        i = 0
        while i < len(book_list):
            self.book_dict[book_list[i]] = [quantity_list[i], price_list[i]]
            i = i + 1

    def check(self, book_name):
        if book_name in self.book_dict.keys():
            return True
        else:
            return False

    def addBook(self, book_name, quantity, price):
        if not self.check(book_name):
           self.book_dict[book_name] = [quantity,price]



books = [5]
qs = [18]
p = [865]
bs = Bookstore(books, qs, p)

bs.addBook("4,68", -18, 108)
print(bs)