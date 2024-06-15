#Создайте класс "Машина" с атрибутами "марка", "модель" и "год выпуска". Напишите метод, который выводит информацию о машине в формате "Марка: марка, Модель: модель, Год выпуска: год".
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Марка: {self.make}, Модель: {self.model}, Год выпуска: {self.year}")

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Ford", "Mustang", 1969)
car1.display_info()
car2.display_info()