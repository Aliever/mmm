numbers = [-3, -2, 0, 4, -1, 5, 6, -7, 8]

first_positive = None
last_negative = None

for num in numbers:
    if first_positive == None:  # ещё не нашли первый положительный
        if num > 0:
            first_positive = num  # нашли первый положительный

    if num < 0:
        last_negative = num  # каждый раз запоминаем отрицательное число

print("Первый положительный элемент:", first_positive)
print("Последний отрицательный элемент:", last_negative)
