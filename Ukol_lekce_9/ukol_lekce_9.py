#task1
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


  # Metoda pro výstup dat
    def display_info(self):
        print(f"Model: {self.__model}")
        print(f"Year: {self.__year}")
        print(f"Manufacturer: {self.__manufacturer}")
        print(f"Engine Volume: {self.__engine_volume} L")
        print(f"Color: {self.__color}")
        print(f"Price: ${self.__price}")

# Příklad použití
car1 = Car("Octavia", 2022, "Skoda", 2.0, "White", 41888)
car2 = Car("Mustang", 2021, "Ford", 5.0, "Blue", 55999)

car1.display_info()
print("---")
car2.display_info()

# Změna a získání hodnot
car1.set_color("Black")
print(f"Updated color of car1: {car1.get_color()}")

print()
#task 2
class TemperatureConverter:
    conversion_count = 0  # Statická proměnná pro sledování počtu převodů

    def __init__(self):
        pass

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.conversion_count += 1
        return celsius * 9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.conversion_count += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def bulk_celsius_to_fahrenheit(celsius_list):
        return [TemperatureConverter.celsius_to_fahrenheit(c) for c in celsius_list]

    @staticmethod
    def bulk_fahrenheit_to_celsius(fahrenheit_list):
        return [TemperatureConverter.fahrenheit_to_celsius(f) for f in fahrenheit_list]

    @staticmethod
    def get_conversion_count():
        return TemperatureConverter.conversion_count

# Příklad použití
converter = TemperatureConverter()

# Převod jednotlivých teplot
temp_c = 100
temp_f = converter.celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C je {temp_f}°F")

temp_f = 212
temp_c = converter.fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F je {temp_c}°C")

# Hromadný převod jednotek
celsius_temps = [0, 25, 100]
fahrenheit_temps = [32, 77, 212]

converted_to_fahrenheit = converter.bulk_celsius_to_fahrenheit(celsius_temps)
converted_to_celsius = converter.bulk_fahrenheit_to_celsius(fahrenheit_temps)
print()
print(f"Teploty v °C: {celsius_temps} převedené na °F: {converted_to_fahrenheit}")
print(f"Teploty v °F: {fahrenheit_temps} převedené na °C: {converted_to_celsius}")
print()
print(f"Počet provedených převodů: {converter.get_conversion_count()}")