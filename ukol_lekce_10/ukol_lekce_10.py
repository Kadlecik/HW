#task1/1
class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Power: {self.power}W")

class CoffeeMachine(Device):
    def __init__(self, brand, model, power, water_capacity, coffee_type):
        super().__init__(brand, model, power)
        self.water_capacity = water_capacity
        self.coffee_type = coffee_type

    def make_coffee(self):
        print(f"Making a cup of {self.coffee_type} coffee...")

    def display_info(self):
        super().display_info()
        print(f"Water Capacity: {self.water_capacity}L")
        print(f"Coffee Type: {self.coffee_type}")

class Blender(Device):
    def __init__(self, brand, model, power, blade_material, speed_settings):
        super().__init__(brand, model, power)
        self.blade_material = blade_material
        self.speed_settings = speed_settings

    def blend(self):
        print("Blending ingredients...")

    def display_info(self):
        super().display_info()
        print(f"Blade Material: {self.blade_material}")
        print(f"Speed Settings: {self.speed_settings}")

class MeatGrinder(Device):
    def __init__(self, brand, model, power, grinder_size, safety_features):
        super().__init__(brand, model, power)
        self.grinder_size = grinder_size
        self.safety_features = safety_features

    def grind_meat(self):
        print("Grinding meat...")

    def display_info(self):
        super().display_info()
        print(f"Grinder Size: {self.grinder_size}")
        print(f"Safety Features: {self.safety_features}")

# Příklad použití tříd
coffee_machine = CoffeeMachine("DeLonghi", "Magnifica", 1450, 1.8, "Espresso")
blender = Blender("NutriBullet", "Pro 900", 900, "Stainless Steel", 3)
meat_grinder = MeatGrinder("Bosch", "MFW67440", 700, "5mm", "Safety Lock")

coffee_machine.display_info()
coffee_machine.make_coffee()
print()
blender.display_info()
blender.blend()
print()
meat_grinder.display_info()
meat_grinder.grind_meat()


#task2/1+2
import time

def display_time():
    return time.strftime("%H:%M")

def display_date():
    return time.strftime("%d.%m.%Y")

def decorate_function(func):
    def wrapper():
        print("*" * 20)
        print(func())
        print("*" * 10)
    return wrapper

def decorate_with_hashes(func):
    def wrapper():
        print("#" * 10)
        print(func())
        print("#" *20)
    return wrapper
# Použití funkce
print()

decorated_display_time = decorate_function(display_time)
decorated_display_date = decorate_with_hashes(display_date)

decorated_display_time()
decorated_display_date()

#task2/3
import time

def display_time():
    return time.strftime("%H:%M")

def display_date():
    return time.strftime("%d.%m.%Y")

def decorate_with_stars(func):
    def wrapper():
        print("<" * 20)
        print(func())
        print("<" * 10)
    return wrapper

def decorate_with_hashes(func):
    def wrapper():
        print(">" * 10)
        print(func())
        print(">" * 20)
    return wrapper

# Použití dekorátorů pomocí syntaxe dekorátoru
@decorate_with_stars
def decorated_time():
    return display_time()

@decorate_with_hashes
def decorated_date():
    return display_date()
print()
decorated_time()
decorated_date()
