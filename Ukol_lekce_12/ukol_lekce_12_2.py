import json
import pickle

class Car:
    def __init__(self, brand, model, year, color):
        """
        Inicializace objektu třídy Car.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def to_dict(self):
        """Převede objekt auta na slovník."""
        return {
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "color": self.color
        }

    @classmethod
    def from_dict(cls, data):
        """Vytvoří objekt auta ze slovníku."""
        return cls(data["brand"], data["model"], data["year"], data["color"])

    def save_to_json(self, file_path=None):
        """
        Ukládá objekt do formátu JSON.
        Pokud je zadána cesta, uloží výstup do souboru.
        """
        car_json = json.dumps(self.to_dict(), indent=4)
        if file_path:
            with open(file_path, 'w') as file:
                file.write(car_json)
            print(f"Data byla uložena do JSON souboru: {file_path}")
        return car_json

    @classmethod
    def load_from_json(cls, json_data):
        """
        Načítá objekt z JSON dat.
        Může přijmout buď string, nebo cestu k JSON souboru.
        """
        if isinstance(json_data, str):
            try:
                with open(json_data, 'r') as file:
                    data = json.load(file)
                print(f"Data načtena ze souboru: {json_data}")
            except FileNotFoundError:
                data = json.loads(json_data)
        else:
            raise ValueError("Neplatný vstup. Poskytněte JSON string nebo cestu k souboru.")
        return cls.from_dict(data)

    def save_to_pickle(self, file_path):
        """
        Ukládá objekt pomocí Pickle a uloží jej do souboru.
        """
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)
        print(f"Data byla uložena do Pickle souboru: {file_path}")

    @classmethod
    def load_from_pickle(cls, file_path):
        """
        Načítá objekt z Pickle souboru.
        """
        with open(file_path, 'rb') as file:
            car = pickle.load(file)
        print(f"Data načtena z Pickle souboru: {file_path}")
        return car


# Příklad použití
if __name__ == "__main__":
    car = Car("Skoda", "Elroq", 2024, "green")

    # Ukládání a načítání pomocí JSON
    print("=== JSON ===")
    json_data = car.save_to_json("car.json")
    new_car_json = Car.load_from_json("car.json")
    print(f"Načteno z JSON: {new_car_json.to_dict()}")

    # Ukládání a načítání pomocí Pickle
    print("\n=== Pickle ===")
    car.save_to_pickle("car.pkl")
    new_car_pickle = Car.load_from_pickle("car.pkl")
    print(f"Načteno z Pickle: {new_car_pickle.to_dict()}")
