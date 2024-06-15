import re

with open('dates1.txt.txt', 'r') as file:
    data = file.read()
dates = re.findall(r'\b(\d{2}).02.(\d{4})\b', data)
with open('february_dates.txt', 'w') as new_file:
    for date in dates:
        formatted_date = f'{date[0]}/02/{date[1]}\n'
        new_file.write(formatted_date)