class Calculator:

    @staticmethod
    def add(num1: float, num2: float) -> float:
        return num1 + num2

    @staticmethod
    def subtract(num1: float, num2: float) -> float:
        return num1 - num2

    @staticmethod
    def multiply(num1: float, num2: float) -> float:
        return num1 * num2

    @staticmethod
    def divide(num1: float, num2: float) -> float:
        return num1 / num2

    @staticmethod
    def exponent(num1: float, num2: float) -> float:
        return num1 ** num2


calculator = Calculator()
print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))
print(calculator.exponent(3, 2))
