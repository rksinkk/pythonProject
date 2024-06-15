#2. Из предложенного текстового файла (text18-14.txt) вывести на экран его содержимое,
#количество пробельных символов. Сформировать новый файл, в который поместить текст в
#стихотворной форме предварительно заменив символы третей строки их числовыми кодами
f = open("text18-14.txt", "r", encoding="utf-8")
text = f.read()
f.close()
print(text)
print(f)
spaces = len(text.split(" "))-1
print(f" Количество пробелов:{spaces}")
line = ""
for i in text.split("\n")[2]:
    line += str(ord(i))

f2 = open("text18-14-2.txt", "w+", encoding="utf-8")
f2.write(text.replace("Богатыри — не вы.", line))
f2.close()