def numbers():
    number = int(input("Введите число: ")) #проверяемое число
    num_str = str(number) #преобразуем в строку, чтобы перебрать каждую цифру
    for i in range(len(num_str) - 1):  #Перебираю индексы цифр в числе
        if num_str[i] < num_str[i + 1]: #сравниваю текущую цифру со следующей
            return "Цифры числа не расположены по убыванию."

        elif num_str[i] == num_str[i + 1]:
            return "Цифры равны."

        else:
            return "Цифры числа расположены по убыванию."

result = numbers()
print(result)