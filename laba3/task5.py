def positive_num():
    #Ввод элементов массива
    array = []
    n = int(input("Введите количество чисел в массиве: ")) #Кол-во элементов в массиве
    for i in range(n): #генерируем массив с n колвом итераций
        num = int(input("Введите числа: ")) #Вводим свои числа в массив
        array.append(num) #Добавим число в массив
        #счетчик положительных чисел
    counter = 0
    for number in array:
        if number > 0:
            counter += 1

    print("Количество положительных чисел", counter)
positive_num()