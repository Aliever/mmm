from datetime import datetime


def format_date(input_date):
    try:
        # Преобразуем входную строку в объект datetime
        date_object = datetime.strptime(input_date, "%d.%m.%Y")

        # Форматируем дату в нужном формате
        formatted_date = date_object.strftime("%A, %d %B, %Y")

        return formatted_date
    except ValueError:
        return "Ошибка: Неверный формат даты. Пожалуйста, используйте формат dd.mm.yyyy."


# Пример использования функции
input_date = input("Введите дату (dd.mm.yyyy): ")
output_date = format_date(input_date)
print(output_date)