#С помощью функций получить вертикальную и горизонтальную линии. Линия проводится многократной печатью полученных линий. символа. Заключить слово В рамку из полученных линий.
def h(l):
    print("+" + "-" * l + "+")
def v(s):
    print("|" + s + "|")
h(len(s := input("Введите слово: "))); v(s); h(len(s))