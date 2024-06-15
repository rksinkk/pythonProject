#Для задачи из блока 1 создать две функции, save_defи load def, которые позволяют сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно. Использовать модуль pickle для сериализации и десериализации объектов Python в бинарном формате
import pickle

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Марка: {self.make}, Модель: {self.model}, Год выпуска: {self.year}")

def save_def(cars, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(cars, file)
        print("Информация успешно сохранена в файл.")
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")

def load_def(filename):
    try:
        with open(filename, 'rb') as file:
            cars = pickle.load(file)
        print("Информация успешно загружена из файла.")
        return cars
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        return []
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Ford", "Mustang", 1969)
car3 = Car("Honda", "Civic", 2018)
cars = [car1, car2, car3]
save_def(cars, 'cars.pkl')
loaded_cars = load_def('cars.pkl')
for car in loaded_cars:
    car.display_info()