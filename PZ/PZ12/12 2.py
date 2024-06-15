#Составить генератор (yield), который выводит из строки только цифры.
def brand_new_iterator(s):
    for i in s:
        if str(i) in "0123456789":
            yield i
gen = brand_new_iterator(input("Введите строку:"))
for i in gen:
    print(i)