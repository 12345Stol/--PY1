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
        """
        Создание и подготовка к работе объекта "Книга"
        :param id_: идентификатор книги
        :param name: название книги
        :param pages: количество страниц в книге
        """
        if not isinstance(id_, int):
            raise TypeError("Значение id должно быть целым числом")
        if id_ <= 0:
            raise ValueError("Недопустимое значение id")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("Значение name должно быть строкой")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Значение pages должно быть целым числом")
        if pages <= 0:
            raise ValueError("Недопустимое значение pages")
        self.pages = pages


class Library:
    def __init__(self, books: list[Book] = []):
        """
        Создание и подготовка к работе объекта "Библиотека"
        :param books: список книг
        """
        if not isinstance(books, list):
            raise TypeError("Значение books должно быть списком")
        self.books = books

    def get_next_book_id(self) -> int:
        if not self.books:  # Если список книг пуст
            return 1  # То выводим значение 1
        else:
            return self.books[-1].id_ + 1  # Иначе к значению id последней книги прибавляем 1

    def get_index_by_book_id(self, _id_: int) -> int:
        if not isinstance(_id_, int):
            raise TypeError("Значение индекса книги _id_ должно быть целым числом")
        if _id_ <= 0:
            raise ValueError("Недопустимое значение индекса книги _id_")

        for index_dict, dict_ in enumerate(self.books):  # перебираем все книги в списке и их индексы
            if dict_.id_ == _id_:  # Проверяем есть искомое значение id книги
                return index_dict  # Если да, то выводим индекс книги в списке
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
