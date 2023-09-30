import csv


class InstantiateCSVError(Exception):
    """
    Класс-исключение, возникает, если файл поврежден
    """
    def __init__(self, *args, **kwargs):
        self.massage = "Файл item.csv поврежден"


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(\'{self.name}\', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return self.__name

    @classmethod
    def instantiate_from_csv(cls, path="../src/items.csv"):
        """класс-метод, инициализирующий экземпляры
         класса `Item` данными из файла _src/items.csv_"""
        try:
            with open(path, newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                try:
                    for row in reader:
                        item = cls(str(row['name']), float(row['price']), int(row['quantity']))
                except KeyError:
                    raise InstantiateCSVError
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        except InstantiateCSVError:
            raise InstantiateCSVError("Файл item.csv поврежден")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self.__name = value[0:10]
        else:
            self.__name = value

    @staticmethod
    def string_to_number(string) -> int:
        """
        Cтатический метод, возвращает число из числа-строки
        """
        return int(string[0])

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

        return self.price

    def __add__(self, other):
        """
        Складывает количество товара экземпляров класса Item и дочерних от них
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError("Складывать можно только экземпляры класса Item и дочерние от них")

