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


    def addQuantity(self, book_name, quantity):
        if self.check(book_name):
            self.book_dict[book_name][0] += quantity


    def adjustPrice(self, book_name, price):
        if self.check(book_name):
            self.book_dict[book_name][1] = price


    def getQuantity(self, book_name):
        if self.check(book_name):
            return self.book_dict[book_name][0]
        else:
            return None

    def getPrice(self, book_name):
        if self.check(book_name):
            return self.book_dict[book_name][1]
        else:
            return None



