#Создайте базовый класс "Форма" со свойствами "цвет" и "тип". От этого класса унаследуйте класс "Круг" и добавьте в него свойство "радиус". Определите методы вычисления площади и периметра.
import tkinter as tk
import math

class Shape:
    def __init__(self, color, shape_type):
        self.color = color
        self.shape_type = shape_type

    def display_info(self):
        return f"Цвет: {self.color}, Тип: {self.shape_type}"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color, "Круг")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def display_info(self):
        return (super().display_info() +
                f", Радиус: {self.radius}, Площадь: {self.area():.2f}, Периметр: {self.perimeter():.2f}")

def show_circle_info():
    color = color_entry.get()
    radius = float(radius_entry.get())
    circle = Circle(color, radius)
    result_label.config(text=circle.display_info())

root = tk.Tk()
root.title("Circle Information")

tk.Label(root, text="Цвет").grid(row=0)
tk.Label(root, text="Радиус").grid(row=1)

color_entry = tk.Entry(root)
radius_entry = tk.Entry(root)

color_entry.grid(row=0, column=1)
radius_entry.grid(row=1, column=1)

tk.Button(root, text="Показать информацию", command=show_circle_info).grid(row=2, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2)

root.mainloop()