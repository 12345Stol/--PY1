class Exams:
    """ Базовый класс Экзамены.
    :param name: Имя ученика
    :param rus: Балл за экзамен по русскому языку
    :param math: Балл за экзамен по математике
    :param rus_mark: Проходной балл по русскому языку
    :param math_mark: Проходной балл по математике
    """
    def __init__(self, name: str, rus: int, math: int, rus_mark: int, math_mark: int):
        """
        Применяются protected атрибуты.
        Инкапсуляция позволяет контролировать доступ к переменным атрибутам, чтобы они не принимали недопустимые значения.
        Имя ученика всегда должно быть типа str, баллы - типа int и должны находится в определнном диапозоне.
        """
        self._name = name  # Отработает setter свойства
        self._rus = rus  # Отработает setter свойства
        self._math = math  # Отработает setter свойства
        self._rus_mark = rus_mark  # Отработает setter свойства
        self._math_mark = math_mark  # Отработает setter свойства

    @property
    def name(self) -> str:
        """ Возращает имя ученика"""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """ Устанавливает имя ученика"""
        if not isinstance(new_name, str):
            raise TypeError("Имя ученика должно быть типа str")
        self._name = new_name

    @property
    def rus(self) -> int:
        """ Возращает балл за экзамен по русскому языку"""
        return self._rus

    @rus.setter
    def rus(self, new_rus: int) -> None:
        """ Устанавливает балл за экзамен по русскому языку"""
        if not isinstance(new_rus, int):
            raise TypeError("Балл за экзамен по русскому языку должен быть типа int")
        if new_rus <= 0 or new_rus > 100:
            raise ValueError("Недопустимое значение балла за экзамен по русскому языку")
        self._rus = new_rus

    @property
    def math(self) -> int:
        """ Возращает балл за экзамен по математике"""
        return self._math

    @math.setter
    def math(self, new_math: int) -> None:
        """ Устанавливает балл за экзамен по математике"""
        if not isinstance(new_math, int):
            raise TypeError("Балл за экзамен по математике должен быть типа int")
        if new_math <= 0 or new_math > 100:
            raise ValueError("Недопустимое значение балла за экзамен по математике")
        self._math = new_math

    @property
    def rus_mark(self) -> int:
        """ Возращает проходной балл по русскому языку"""
        return self._rus_mark

    @rus_mark.setter
    def rus_mark(self, new_rus_mark: int) -> None:
        """ Устанавливает проходной балл по русскому языку"""
        if not isinstance(new_rus_mark, int):
            raise TypeError("Проходной балл по русскому языку должен быть типа int")
        if new_rus_mark <= 0 or new_rus_mark > 100:
            raise ValueError("Недопустимое значение проходного балла по русскому языку")
        self._rus_mark = new_rus_mark

    @property
    def math_mark(self) -> int:
        """ Возращает проходной балл по математике"""
        return self._math_mark

    @math_mark.setter
    def math_mark(self, new_math_mark: int) -> None:
        """ Устанавливает проходной балл по математике"""
        if not isinstance(new_math_mark, int):
            raise TypeError("Проходной балл по математике должен быть типа int")
        if new_math_mark <= 0 or new_math_mark > 100:
            raise ValueError("Недопустимое значение проходного балла по математике")
        self._math_mark = new_math_mark

    def __str__(self):
        return f"Ученик {self.name}. Баллы по общеобразовательным предметам : русский язык - {self.rus}, математика - {self.math}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, rus={self.rus!r}, math={self.math!r}, rus_mark={self.rus_mark!r}, math_mark={self.math_mark!r})"

    def graduate_from_school(self) -> str:
        """
        Метод проверяет сможет ли ученик успешно закончить школу по результам экзаменов
        :return: Сможет ли ученик успешно закончить или же останется на второй год
        """
        if self.rus >= self.rus_mark and self.math >= self.math_mark:
            return 'Ученик успешно закончил школу.'
        else:
            return 'Ученик остался на второй год.'

    def entering_university(self) -> str:
        """
        Метод проверяет сможет ли ученик продолжить обучение, сдав минимальный список общеобразовательных предметов. Продолжить обучение с таким набором предметов можно только в колледже
        :return: Сможет ли ученик продолжить обучение после школы
        """
        if self.rus >= self.rus_mark and self.math >= self.math_mark:
            return 'Ученик сможет продолжить учиться (как минимум в колледже)'
        else:
            return 'Ученик не сможет продолжить обучение'


class TechnicalExams(Exams):
    """ Дочерний класс Технические экзамены.
        :param name: Имя ученика
        :param rus: Балл за экзамен по русскому языку
        :param math: Балл за экзамен по математике
        :param rus_mark: Проходной балл по русскому языку
        :param math_mark: Проходной балл по математике
        :param physics: Балл за экзамен по физике
        :param physics_mark: Проходной балл по физике
        """
    def __init__(self, name: str, rus: int, math: int, rus_mark: int, math_mark: int, physics: int, physics_mark: int ):
        """
        Применяются protected атрибуты.
        Инкапсуляция позволяет контролировать доступ к переменным атрибутам, чтобы они не принимали недопустимые значения.
        Баллы должны быть всегда типа int и должны находится в определнном диапозоне.
        """
        super().__init__(name, rus, math, rus_mark, math_mark)  # Наследование конструктора базового класса
        self._physics = physics  # Расширение конструктора базового класса. Добавление атрибута
        self._physics_mark = physics_mark  # Расширение конструктора базового класса. Добавление атрибута

    @property
    def physics(self) -> int:
        """ Возращает балл за экзамен по физике"""
        return self._physics

    @physics.setter
    def physics(self, new_physics: int) -> None:
        """ Устанавливает балл за экзамен по физике"""
        if not isinstance(new_physics, int):
            raise TypeError("Балл за экзамен по физике должен быть типа int")
        if new_physics <= 0 or new_physics > 100:
            raise ValueError("Недопустимое значение балла за экзамен по физике")
        self._physics = new_physics

    @property
    def physics_mark(self) -> int:
        """ Возращает проходной балл по физике"""
        return self._physics_mark

    @physics_mark.setter
    def physics_mark(self, new_physics_mark: int) -> None:
        """ Устанавливает проходной балл по физике"""
        if not isinstance(new_physics_mark, int):
            raise TypeError("Проходной балл по физике должен быть типа int")
        if new_physics_mark <= 0 or new_physics_mark > 100:
            raise ValueError("Недопустимое значение проходного балла по физике")
        self._physics = new_physics_mark

    def __repr__(self):  # Метод __repr__ перегружен, так как в дочернем классе появляется два новых атрибута
        return f"{self.__class__.__name__}(name={self.name!r}, rus={self.rus!r}, math={self.math!r}, rus_mark={self.rus_mark!r}, math_mark={self.math_mark!r}, physics={self.physics!r}, physics_mark={self.physics_mark!r} )"

    def entering_university(self) -> str:
        """
        Метод проверяет сможет ли ученик продолжить обучение, сдав дополнительно предмет: физику
        Метод перегружен, так как в дочернем классе появляется возможность поступить не только в колледж, но и в технический университет
        :return: Сможет ли ученик продолжить обучение и если сможет то поступит ли в технический университет
        """

        if self.physics >= self.physics_mark and self.rus >= self.rus_mark and self.math >= self.math_mark:
            return 'Ученик сможет продолжить учиться в техничесиком университете'
        elif self.rus <= self.rus_mark or self.math <= self.math_mark:
            return 'Ученик не сможет продолжить обучение'
        else:
            return 'Ученик не сможет обучаться в техничесиком университете, но сможет пойти в колледж'


class HumanitarianExams(Exams):
    """ Дочерний класс Гуманитарные экзамены.
        :param name: Имя ученика
        :param rus: Балл за экзамен по русскому языку
        :param math: Балл за экзамен по математике
        :param rus_mark: Проходной балл по русскому языку
        :param math_mark: Проходной балл по математике
        :param social_science: Балл за экзамен по обществознанию
        :param social_science_mark: Проходной балл по обществознанию
        """
    def __init__(self, name: str, rus: int, math: int, rus_mark: int, math_mark: int, social_science: int, social_science_mark: int):
        """
        Применяются protected атрибуты.
        Инкапсуляция позволяет контролировать доступ к переменным атрибутам, чтобы они не принимали недопустимые значения.
        Баллы должны быть всегда типа int и должны находится в определнном диапозоне.
        """
        super().__init__(name, rus, math, rus_mark, math_mark)  # Наследование конструктора базового класса
        self._social_science = social_science  # Расширение конструктора базового класса. Добавление атрибута
        self._social_science_mark = social_science_mark  # Расширение конструктора базового класса. Добавление атрибута

    @property
    def social_science(self) -> int:
        """ Возращает балл за экзамен по обществознанию"""
        return self._social_science

    @social_science.setter
    def social_science(self, new_social_science: int) -> None:
        """ Устанавливает балл за экзамен по обществознанию"""
        if not isinstance(new_social_science, int):
            raise TypeError("Балл за экзамен по обществознанию должен быть типа int")
        if new_social_science <= 0 or new_social_science > 100:
            raise ValueError("Недопустимое значение балла за экзамен по обществознанию")
        self._social_science = new_social_science

    @property
    def social_science_mark(self) -> int:
        """ Возращает проходной балл по обществознанию"""
        return self._social_science_mark

    @social_science_mark.setter
    def social_science_mark(self, new_social_science_mark: int) -> None:
        """ Устанавливает проходной балл по обществознанию"""
        if not isinstance(new_social_science_mark, int):
            raise TypeError("Проходной балл по обществознанию должен быть типа int")
        if new_social_science_mark <= 0 or new_social_science_mark > 100:
            raise ValueError("Недопустимое значение проходного балла по обществознанию")
        self._social_science_mark = new_social_science_mark

    def __repr__(self):  # Метод __repr__ перегружен, так как в дочернем классе появляется два новых атрибута
        return f"{self.__class__.__name__}(name={self.name!r}, rus={self.rus!r}, math={self.math!r}, rus_mark={self.rus_mark!r}, math_mark={self.math_mark!r}, social_science={self.social_science!r}, social_science_mark={self.social_science_mark!r} )"

    def entering_university(self) -> str:
        """
        Метод проверяет сможет ли ученик продолжить обучение, сдав дополнительно предмет: обществознание
        Метод перегружен, так как в дочернем классе появляется возможность поступить не только в колледж, но и в гуманитарный университет
        :return: Сможет ли ученик продолжить обучение и если сможет то поступит ли в гуманитарный университет
        """
        if self.social_science >= self.social_science_mark and self.rus >= self.rus_mark and self.math >= self.math_mark:
            return 'Ученик сможет продолжить учиться в гуманитарном университете'
        elif self.rus <= self.rus_mark or self.math <= self.math_mark:
            return 'Ученик не сможет продолжить обучение'
        else:
            return 'Ученик не сможет обучаться в гуманитарном университете, но сможет пойти в колледж'


if __name__ == "__main__":
    student_1 = TechnicalExams('Женя', 65, 65, 60, 60, 80, 75)  # Сможет поступить в технический университет
    print(student_1)
    print(student_1.graduate_from_school(), student_1.entering_university())
    print()
    student_2 = HumanitarianExams('Олег', 57, 55, 60, 60, 98, 80)  # Останется на второй год и не сможет продолжить обучение
    print(student_2)
    print(student_2.graduate_from_school(), student_2.entering_university())
    print()
    student_3 = HumanitarianExams('Лиза', 70, 74, 60, 60, 61, 80)   # Сможет поступить только в колледж
    print(student_3)
    print(student_3.graduate_from_school(), student_3.entering_university())
    print()
    student_4 = Exams('Зина', 90, 90, 60, 60)  # Сможет продолжить обучение
    print(student_4)
    print(student_4.graduate_from_school(), student_4.entering_university())

