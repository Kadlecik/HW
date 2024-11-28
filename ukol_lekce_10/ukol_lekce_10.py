#task1
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