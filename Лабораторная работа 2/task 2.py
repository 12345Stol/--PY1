from typing import Optional
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages


class Library:
    def __init__(self, books: list[Book] = None):
        self.books = books
        if books is None:
            self.books = []

    def get_next_book_id(self) -> int:
        if not self.books:  # Если список книг пуст
            return 1  # То выводим значение 1
        else:
            return self.books[-1].id_ + 1  # Иначе к значению id последней книги прибавляем 1

    def get_index_by_book_id(self, _id_: int) -> int:
        for index_dict, dict_ in enumerate(self.books):  # перебираем все книги в списке и их индексы
            if dict_.id_ == _id_:  # Проверяем есть искомое значение id книги
                return index_dict  # Если да, то выводим индекс книги в списке
            else:
                raise ValueError('Книги с запрашиваемым id не существует')  # Если нет, то выводим ошибку


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

