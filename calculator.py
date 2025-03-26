class Calculator:
    def add(self, a, b):
        """Suma dos números."""
        return a + b

    def subtract(self, a, b):
        """Resta dos números."""
        return a - b

    def multiply(self, a, b):
        """Multiplica dos números."""
        return a * b

    def divide(self, a, b):
        """Divide dos números, validando la división por cero."""
        if b == 0:
            raise ValueError("Error: No se puede dividir entre cero.")
        return a / b

# Ejemplo de uso
if __name__ == "__main__":
    calc = Calculator()
    try:
        print("Suma: ", calc.add(10, 5))
        print("Resta: ", calc.subtract(10, 5))
        print("Multiplicación: ", calc.multiply(10, 5))
        print("División: ", calc.divide(10, 0))  # Cambia el segundo argumento para probar
    except ValueError as e:
        print(e)