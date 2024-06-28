import re

# Чтение исходного файла
with open('hotline1.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Поиск номеров телефонов
phone_numbers = re.findall(r'8\(\d{3}\)\d{3}-\d{2}-\d{2}', content)
count_phone_numbers = len(phone_numbers)

# Изменение текста
modified_content = content.replace("Горячая линия", "Горячая линия Министерства образования Ростовской области")

# Запись изменённого текста в новый файл
with open('hotline_modified.txt', 'w', encoding='utf-8') as file:
    file.write(modified_content)

# Вывод количества найденных номеров телефонов
print(f"Количество найденных номеров телефонов: {count_phone_numbers}")
