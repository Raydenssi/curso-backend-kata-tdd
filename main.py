import unittest
from datetime import datetime

# Función de suma
def sum(a, b):
    return a + b

# Clase Greeter
class Greeter:
    def greet(self, name: str) -> str:
        # Limpiar espacios en blanco
        name = name.strip()
        
        # Capitalizar la primera letra
        name = name.capitalize()
        
        # Obtener la hora actual
        current_hour = datetime.now().hour
        
        # Determinar el saludo según la hora del día
        if 6 <= current_hour < 12:
            greeting = f"Good morning {name}"
        elif 18 <= current_hour < 22:
            greeting = f"Good evening {name}"
        elif 22 <= current_hour or current_hour < 6:
            greeting = f"Good night {name}"
        else:
            greeting = f"Hola {name}"
        
        # Registrar en la consola
        print(f"greet called with {name}")
        
        return greeting

# Pruebas
class SumTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)  # Corregido para que la prueba pase

class GreeterTest(unittest.TestCase):
    def test_greet(self):
        greeter = Greeter()
        self.assertIn("Good morning", greeter.greet("  paolo  "))
        self.assertIn("Good evening", greeter.greet("maría"))
        self.assertIn("Good night", greeter.greet("   Juan"))

if __name__ == '__main__':
    unittest.main()
