#Дан номер года (положительное целое число). Определить количество дней в этом году, учитывая, что обычный год насчитывает 365 дней, а високосный - 366 дней. Високосным считается год делится на 4, за исключением тех лет, которые подразделяются на 100 и не делятся на 400 (например, годы 300, 1300 1900 не является високосными, а 1200 и 2000 - являются).
n = input("Введите номер года:")
try:
    n =int(n)
    if n > 0:
        if n % 4 != 0:
            print('365')
        elif n % 100 != 0:
            print('366')
        elif n % 400 != 0:
            print('365')
        else:
            print('366')
    else:
        print("Введите корректный год")
except ValueError:
    print("Вводите только числа")