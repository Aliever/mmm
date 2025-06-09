def even_elements():
    user_input = input("Введите элементы списка через пробел: ")
    elements = list(map(int, user_input.split())) #Создаем список из введенных элементов
    product = 1 #Произведение
    for i in range(len(elements)): #Перебираем все индексы элементов списка
        if i % 2 != 0: #Проверяем, является ли индекс нечетным
            product *= elements[i] #Умножнаем на элемент с нечетным индексом
    return product

result = even_elements()
print("Произведение чисел с нечетными индексами: ", result)