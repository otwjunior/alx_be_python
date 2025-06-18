class Book:
    def __init__(self,title,author):
        self.title = title
        self.author= author
        self.__is_checked_out =False

    def check_out(self):
        if self.__is_checked_out == False:
            self.__is_checked_out = True
           # print('borrowed')
            return True
        #print('available to borrow')
        return False
    
    def return_book(self):
        if self.__is_checked_out == True:
            self.__is_checked_out = False
            return True
        return False
    def is_available(self):
         return True if self.__is_checked_out == False else False
class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self,book):
        self._books.append(book)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f'you borrowed "{title}".')
                    return
                else:
                    print(f'"{title}" is already checked out.')
                    return
        print(f'Book titled {title} not found in libraly')
    def return_book(self,title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    #print(f'Thanks yoou for returning {title} in good condition')
                    return
                else:
                    print(f'{title} was not checked out.')
                    return
        print(f'Book titled{title} not found in the libraly.')
    
    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f'{book.title} by {book.author}')

