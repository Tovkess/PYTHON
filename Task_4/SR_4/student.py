class Student:
    def __init__(self, full_name, group_number, birth_date=None):
        self.__full_name = full_name
        self.__group_number = group_number
        self.__birth_date = birth_date

    # Геттери
    @property
    def full_name(self):
        return self.__full_name

    @property
    def group_number(self):
        return self.__group_number

    @property
    def birth_date(self):
        return self.__birth_date

    # Сеттери
    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @group_number.setter
    def group_number(self, value):
        self.__group_number = value

    @birth_date.setter
    def birth_date(self, value):
        self.__birth_date = value

    def __str__(self):
        return f"{self.__full_name}, Група: {self.__group_number}"