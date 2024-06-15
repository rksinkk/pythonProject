#Создайте класс "Машина" с атрибутами "марка", "модель" и "год выпуска". Напишите метод, который выводит информацию о машине в формате "Марка: марка, Модель: модель, Год выпуска: год"
import tkinter as tk

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"Марка: {self.make}, Модель: {self.model}, Год выпуска: {self.year}"

def show_car_info():
    make = make_entry.get()
    model = model_entry.get()
    year = year_entry.get()
    car = Car(make, model, year)
    result_label.config(text=car.display_info())

root = tk.Tk()
root.title("Car Information")

tk.Label(root, text="Марка").grid(row=0)
tk.Label(root, text="Модель").grid(row=1)
tk.Label(root, text="Год выпуска").grid(row=2)

make_entry = tk.Entry(root)
model_entry = tk.Entry(root)
year_entry = tk.Entry(root)

make_entry.grid(row=0, column=1)
model_entry.grid(row=1, column=1)
year_entry.grid(row=2, column=1)

tk.Button(root, text="Показать информацию", command=show_car_info).grid(row=3, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

root.mainloop()