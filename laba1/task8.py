date_str = "2025-12-31"  # исходная дата
year, month, day = date_str.split('-')  # Разделяем строку по символу "-", через каждый "-" будет отделяться и присваиваться переменной

# Создаем словарь с нужными значениями
date_dict = {
    "Year": year,
    "Month": month,
    "Day": day
}

print(date_dict)