import random


def generation_array():
    n = random.randint(1, 25)  # Генерируем случайную длину массива
    print("Длина массива: ", n)
    array = []

    while True:  # Запрашиваем у пользователя начальное число и проверяем, кратно ли оно 3
        start_number = int(input(
            "Введите с какой точки вы хотите видеть числа расположенные по убыванию, которые делятся на 3 без остатка: "))
        if start_number % 3 == 0:
            break  # Закончим цикл, и перейдем к циклу for
        else:
            print("Ошибка: число должно быть кратно 3. Попробуйте снова.")

    for i in range(n):
        array.append(start_number)  # Добавляем текущее число в массив
        start_number -= 3  # Уменьшаем на 3 для следующего элемента

    return array


generated_array = generation_array()
print("Сгенерированный массив: ", generated_array)