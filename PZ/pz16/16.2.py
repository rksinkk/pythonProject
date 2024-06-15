#Создайте базовый класс "Форма" со свойствами "цвет" и "тип". От этого класса унаследуйте класс "Круг" и добавьте в него свойство "радиус". Определите методы вычисления площади и периметра.
import math

class Shape:
    def __init__(self, color, shape_type):
        self.color = color
        self.shape_type = shape_type

    def display_info(self):
        print(f"Цвет: {self.color}, Тип: {self.shape_type}")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color, "Круг")
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def display_info(self):
        super().display_info()
        print(f"Радиус: {self.radius}, Площадь: {self.calculate_area()}, Периметр: {self.calculate_perimeter()}")
circle = Circle("Красный", 5)
circle.display_info()