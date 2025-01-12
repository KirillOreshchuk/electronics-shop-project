from src.item import Item


class MixinLanguage:
    LANGUAGE = "EN"

    def __init__(self):
        self.__language = "EN"
        MixinLanguage.LANGUAGE = self.__language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        Меняет раскладку клавиатуры с EN на RU и обратно
        """
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"


class Keyboard(Item, MixinLanguage):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
