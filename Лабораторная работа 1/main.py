import doctest


class Students:
    def __init__(self, name: str, mark: int):
        """
        Создание и подготовка к работе объекта "Студенты"
        :param name: имя студента
        :param mark: оценка полученная студентом
        Примеры:
        >>> student = Students ('Анна', 3)  # Инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Недопустимое значение имени")
        self.name = name  # Имя студента

        if not isinstance(mark, int):
            raise TypeError("Оценка должна быть целым числом")
        if mark not in [2, 3, 4, 5]:
            raise ValueError("Недопустимое значение оценки")
        self.mark = mark  # Оценка студента

    def money(self) -> str:
        """
        Функция проверяет получит ли студент стипендию и какую
        :return: Получит ли студент стипендию, если да, то какую
        Пример:
        >>> student = Students ('Анна', 3)
        >>> student.money()
        'не получит стипендию'
        """
        if self.mark == 4:
            return 'получит обычную стипендию'
        elif self.mark == 5:
            return 'получит повышенную стипендию'
        else:
            return 'не получит стипендию'

    def sessia(self) -> str:
        """
        Функция проверяет сдал ли студент сессию
        :return: Сдал ли студент сесиию
        Пример:
        >>> student = Students ('Анна', 3)
        >>> student.sessia()
        'сдал сессию'
        """
        if self.mark >= 3:
            return 'сдал сессию'
        else:
            return 'не сдал сессию, пойдет на пересдачу'

    def diplom(self) -> str:
        """
        Функция проверяет сдал какой диплом может получить студент
        :return: Получит красный или синий диплом
        Пример:
        >>> student = Students ('Анна', 3)
        >>> student.diplom()
        'получит синий диплом'
        """
        if self.mark == 5:
            return 'получит красный диплом'
        else:
            return 'получит синий диплом'


if __name__ == "__main__":
    doctest.testmod()  # Тестирование примеров, которые находятся в документации
student1 = Students('Анна', 2)  # 1-ый экземпляр класса
student2 = Students('Евгений', 4)  # 2-ой экземпляр класса
student3 = Students('Александр', 5)  # 3-ий экземпляр класса
print(student1.name, student1.sessia(), 'и', student1.money(), 'и', student1.diplom())
print(student2.name, student2.sessia(), 'и', student2.money(), 'и', student2.diplom())
print(student3.name, student3.sessia(), 'и', student3.money(), 'и', student3.diplom())


class Parallelepiped:
    def __init__(self, lengh: int, width: int, high: int):
        """
        Создание и подготовка к работе объекта "Параллелепипед"
        :param lengh: длина параллелепипеда
        :param width: ширина параллелепипеда
        :param high: высота параллелепипеда
        Примеры:
        >>> figure = Parallelepiped (40, 50, 60)  # Инициализация экземпляра класса
        """
        if not isinstance(lengh, int):
            raise TypeError("Длина должна быть целым числом")
        if lengh < 0:
            raise ValueError("Недопустимое значение длины")
        self.lengh = lengh  # Длина параллелепипеда

        if not isinstance(width, int):
            raise TypeError("Ширина должна быть целым числом")
        if width < 0:
            raise ValueError("Недопустимое значение ширины")
        self.width = width  # Ширина параллелепипеда

        if not isinstance(high, int):
            raise TypeError("Высота должна быть целым числом")
        if high < 0:
            raise ValueError("Недопустимое значение высоты")
        self.high = high  # Высота параллелепипеда

    def square(self) -> int:
        """
        Функция вычисляет площадь поверхности параллелепипеда
        :return: Значение площади поверхности
        Пример:
        >>> figure = Parallelepiped (40, 50, 60)
        >>> figure.square()
        14800
        """
        return 2 * (self.lengh * self.width + self.lengh * self.high + self.width * self.high)


    def edge(self) -> int:
        """
        Функция вычисляет длину ребер параллелепипеда
        :return: Значение длины ребер параллелепипеда
        Пример:
        >>> figure = Parallelepiped (40, 50, 60)
        >>> figure.edge()
        600
        """
        return 4 * (self.lengh + self.width + self.high)

    def volume(self) -> int:
        """
        Функция вычисляет объем параллелепипеда
        :return: Значение объема параллелепипеда
        Пример:
        >>> figure = Parallelepiped (40, 50, 60)
        >>> figure.volume()
        120000
        """
        return self.lengh * self.width * self.high


if __name__ == "__main__":
    doctest.testmod()  # Тестирование примеров, которые находятся в документации
figure1 = Parallelepiped(10, 15, 5)  # 1-ый экземпляр класса
figure2 = Parallelepiped(1, 2, 3)  # 2-ой экземпляр класса

print('Площадь:', figure1.square(),'Длина ребер:', figure1.edge(),'Объем:', figure1.volume())
print('Площадь:', figure2.square(),'Длина ребер:', figure2.edge(),'Объем:', figure2.volume())


class Tickets:
    def __init__(self, money: int, row: int, expensive_ticket: int, cheap_ticket: int):
        """
        Создание и подготовка к работе объекта "Билеты"
        :param money: количество денег, которые есть в кошельке
        :param row: номер ряда в зале, на который хотелось бы купить билет
        :param expensive_ticket: cтоимость дорогих билетов на 1-3 ряду
        :param cheap_ticket: cтоимость дешевых билетов на остальных рядах
        Примеры:
        >>> ticket = Tickets (800, 7, 2000, 500)  # Инициализация экземпляра класса
        """
        if not isinstance(money, int):
            raise TypeError("Количество денег должно быть целым числом")
        if money < 0:
            raise ValueError("Недопустимое количество денег")
        self.money = money  # Количество имеющихся денег

        if not isinstance(row, int):
            raise TypeError("Номер ряда в зале должена быть целым числом")
        if row < 0:
            raise ValueError("Недопустимое значение номера ряда в зале")
        self.row = row  # Желаемый ряд

        if not isinstance(expensive_ticket, int):
            raise TypeError("Стоимость билета должна быть целым числом")
        if expensive_ticket < 0:
            raise ValueError("Недопустимое значение стоимости билета ")
        self.expensive_ticket = expensive_ticket  # Стоимость дорогих билетов на 1-3 ряд

        if not isinstance(cheap_ticket, int):
            raise TypeError("Стоимость билета должна быть целым числом")
        if cheap_ticket < 0:
            raise ValueError("Недопустимое значение стоимости билета ")
        self.cheap_ticket = cheap_ticket  # Стоимость дешевых билетов

    def ability_to_buy(self) -> str:
        """
        Функция вычисляет хватит ли денег на место в желаемом ряду
        :return: Хватит ли денег или не хватит на покупку билета
        Пример:
        >>> ticket = Tickets (800, 7, 2000, 500)
        >>> ticket.ability_to_buy()
        'Хватит денег на покупку билета'
        """
        if self.money >= self.expensive_ticket or self.money >= self.cheap_ticket:
            if self.row <= 3:
                return 'Хватит денег на покупку билета'
            elif self.row > 3:
                return 'Хватит денег на покупку билета'
        else:
            return 'Не хватит денег на покупку билета'

    def number_of_tickets(self) -> int:
        """
        Функция вычисляет сколько билетов можно купить на имеющиеся деньги 
        :return: Количество билетов
        Пример:
        >>> ticket = Tickets(800, 7, 2000, 500)
        >>> ticket.number_of_tickets()
        1
        """
        if self.row <= 3:
            return self.money // self.expensive_ticket
        elif self.row > 3:
            return self.money // self.cheap_ticket


if __name__ == "__main__":
    doctest.testmod()  # Тестирование примеров, которые находятся в документации
ticket1 = Tickets(5000, 1, 2000, 500)  # 1-ый экземпляр класса
ticket2 = Tickets(200, 15, 3000, 600)  # 2-ой экземпляр класса

print(ticket1.ability_to_buy(),'Можно купить', ticket1.number_of_tickets(), 'билет(а)')
print(ticket2.ability_to_buy(),'Можно купить', ticket2.number_of_tickets(), 'билет(а)')

