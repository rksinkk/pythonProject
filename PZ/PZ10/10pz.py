magistr = {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"}
domknigi = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
bookmarket = {"Пушкин", "Достоевский", "Маяковский"}
galery = {"Чехов", "Тютчев", "Пушкин"}
if "Достоевский" in magistr and "Пушкин" in magistr:
    print("Можно приобрести книги Достоевского и Пушкина в магазине магистр")
    pass
else:
    print("Нету в магистре")
if "Достоевский" in domknigi and "Пушкин" in domknigi:
    print("Можно приобрести книги Достоевского и Пушкина в магазине домкниги")
    pass
else:
    print("Нету в домкниги")
if "Достоевский" in bookmarket and "Пушкин" in bookmarket:
    print("Можно приобрести книги Достоевского и Пушкина в магазине букмастер")
    pass
else:
    print("Нету в букмастер")
if "Достоевский" in galery and "Пушкин" in galery:
    print("Можно приобрести книги Достоевского и Пушкина в магазине галерея")
    pass
else:
    print("Нету в галерея")

galery.add("Грибоедов")
print("Автор Грибоедов добавлен в ассортимент магазина Галерея:", galery)

missing_books = domknigi - galery
print("Книги из магазина ДомКниги, отсутствующие в магазине Галерея:", missing_books)