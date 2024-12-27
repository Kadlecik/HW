class IntegerSet:
    def __init__(self, numbers=None):
        """
        Inicializace IntegerSet s volitelným seznamem čísel.
        """
        self.numbers = set(numbers) if numbers else set()
        print(f"Inicializována množina s prvky: {self.numbers}")

    def add(self, number):
        """Přidá číslo do množiny."""
        self.numbers.add(number)
        print(f"Přidáno číslo {number}. Aktuální množina: {self.numbers}")

    def sum(self):
        """Vrátí součet prvků v množině."""
        result = sum(self.numbers)
        print(f"Součet prvků: {result}")
        return result

    def mean(self):
        """Vrátí aritmetický průměr prvků v množině."""
        if not self.numbers:
            raise ValueError("Nelze spočítat průměr prázdné množiny.")
        result = self.sum() / len(self.numbers)
        print(f"Aritmetický průměr prvků: {result}")
        return result

    def maximum(self):
        """Vrátí maximální prvek v množině."""
        if not self.numbers:
            raise ValueError("Nelze určit maximum prázdné množiny.")
        result = max(self.numbers)
        print(f"Maximální prvek: {result}")
        return result

    def minimum(self):
        """Vrátí minimální prvek v množině."""
        if not self.numbers:
            raise ValueError("Nelze určit minimum prázdné množiny.")
        result = min(self.numbers)
        print(f"Minimální prvek: {result}")
        return result


# Testy pomocí unittest
import unittest

class TestIntegerSet(unittest.TestCase):
    def setUp(self):
        """Příprava prostředí pro testovací případy."""
        self.integer_set = IntegerSet([1, 2, 3, 4, 5])
        print("\n--- Příprava testovacího případu dokončena ---")

    def test_sum(self):
        """Test součtu prvků v množině."""
        print("Testování součtu...")
        self.assertEqual(self.integer_set.sum(), 15)

    def test_mean(self):
        """Test průměru prvků v množině."""
        print("Testování průměru...")
        self.assertEqual(self.integer_set.mean(), 3)

    def test_maximum(self):
        """Test maximálního prvku v množině."""
        print("Testování maxima...")
        self.assertEqual(self.integer_set.maximum(), 5)

    def test_minimum(self):
        """Test minimálního prvku v množině."""
        print("Testování minima...")
        self.assertEqual(self.integer_set.minimum(), 1)

    def test_empty_set(self):
        """Test metod na prázdné množině."""
        print("Testování s prázdnou množinou...")
        empty_set = IntegerSet()
        self.assertEqual(empty_set.sum(), 0)
        with self.assertRaises(ValueError):
            empty_set.mean()
        with self.assertRaises(ValueError):
            empty_set.maximum()
        with self.assertRaises(ValueError):
            empty_set.minimum()

    def test_add(self):
        """Test přidání prvku do množiny."""
        print("Testování přidání prvku...")
        self.integer_set.add(6)
        self.assertIn(6, self.integer_set.numbers)
        self.assertEqual(self.integer_set.sum(), 21)

if __name__ == "__main__":
    unittest.main()
