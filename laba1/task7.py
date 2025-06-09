strings = [  # проверяемые строки
    "http://example.com",
    "sanwich",
    "lexus",
    "https://secure.com"
]

filtered_strings = []  # Создаем новый список

for k in strings:  # перебираем каждую строку
    if k.startswith("http://"):  # startwith проверяет начинается ли строка с указанной части
        filtered_strings.append(k)

print(filtered_strings)