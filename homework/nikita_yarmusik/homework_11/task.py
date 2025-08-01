class Book:
    def __init__(self, title, author, number_of_pages, ISBN, is_reserved):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = ISBN
        self.is_reserved = is_reserved

    material = 'бумага'
    text_availability = True

    def __str__(self):
        status = ', зарезервирована' if self.is_reserved else ''
        return (
            f'Название: {self.title}, Автор: {self.author}, '
            f'страниц: {self.number_of_pages}, материал: {self.material}{status}'
        )


book_1 = Book('Название книги 1', 'Автор 1', 200, '1234567', True)
book_2 = Book('Название книги 2', 'Автор 2', 200, '123452', True)
book_3 = Book('Название книги 3', 'Автор 3', 300, '123453', True)
book_4 = Book('Название книги 4', 'Автор 4', 400, '123454', True)
book_5 = Book('Название книги 5', 'Автор 5', 500, '123455', False)

print(book_1, book_2, book_3, book_4, book_5, sep='\n')


class SchoolBook(Book):
    def __init__(self, title, author, number_of_pages, ISBN, is_reserved, subject, school_year, in_stock):
        super().__init__(title, author, number_of_pages, ISBN, is_reserved)
        self.subject = subject
        self.school_year = school_year
        self.in_stock = in_stock

    def __str__(self):
        status = ', зарезервирована' if self.is_reserved else ''
        return (
            f'Название: {self.title}, Автор: {self.author}, '
            f'страниц: {self.number_of_pages}, предмет: {self.subject}, '
            f'класс: {self.school_year}{status}'
        )


school_book_1 = SchoolBook('Алгебра в примерах', 'Автор 6', 140, '123456', True, 'Алгебра', 10, True)
school_book_2 = SchoolBook('Геометрия для чайников', 'Автор 7', 120, '123457', True, 'Геометрия', 5, False)

print(school_book_1, school_book_2, sep='\n')
