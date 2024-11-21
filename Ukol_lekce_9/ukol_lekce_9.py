class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_volume = engine_volume
        self.__color = color
        self.__price = price

    # Metody pro přístup k jednotlivým polím
    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_manufacturer(self):
        return self.__manufacturer

    def get_engine_volume(self):
        return self.__engine_volume

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def set_engine_volume(self, engine_volume):
        self.__engine_volume = engine_volume

    def set_color(self, color):
        self.__color = color

    def set_price(self, price):
        self.__price = price