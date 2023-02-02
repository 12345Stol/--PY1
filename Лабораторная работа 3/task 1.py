class Book:
    """ Базовый класс книги.
    :param name: Название книги
    :param author: Название книги
    """
    def __init__(self, name: str, author: str):
        self._name = name  # Отработает setter свойства
        self._author = author  # Отработает setter свойства

    @property
    def name(self) -> str:
        """ Возращает название книги"""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """ Устанавливает название книги"""
        if not isinstance(new_name, str):
            raise TypeError("Недопустимое значение названия книги")
        self._name = new_name

    @property
    def author(self) -> str:
        """ Возращает имя автора"""
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        """ Устанавливает имя автора"""
        if not isinstance(new_author, str):
            raise TypeError("Недопустимое значение названия автора")
        self._author = new_author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """
    Дочерний класс "Бумажная книга".
    :param name: Название книги
    :param author: Название автора
    :param pages: Количество страниц
    """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # Вызываем метод родительского класса
        self._pages = pages  # Отработает setter свойства

    @property
    def pages(self) -> int:
        """ Возращает количество страниц книги"""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """ Устанавливает количество страниц книги"""
        if not isinstance(new_pages, int):
            raise TypeError("Недопустимое значение количества страниц")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным чисом")
        self._pages = new_pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"  # Добавим информацию о кол-ве страниц в метод __str__

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})" # Добавим информацию о кол-ве страниц в метод __repr__


class AudioBook(Book):
    """
    Дочерний класс "Аудио книга".
    :param name: Название книги
    :param author: Название автора
    :param duration: Продолжительность книги
    """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # Вызываем метод родительского класса
        self._duration = duration  # Отработает setter свойства

    @property
    def duration(self) -> float:
        """ Возращает продолжительность книги"""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """ Устанавливает продолжительность книги"""
        if not isinstance(new_duration, float):
            raise TypeError("Недопустимое значение продолжительности")
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть положительным чисом")
        self._duration = new_duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"  # Добавим информацию о продолжительности книги в метод __str__

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"  # Добавим информацию о продолжительности книги в метод __repr__
