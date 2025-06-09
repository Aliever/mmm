elements = []
while True:
    user_input = input("Введите элемент или нажмите Enter для завершения:")
    if user_input == "":
        break #выход из цикла
    elements.append(user_input) #добавляем элемент в список

if elements: #проверяем что список не пуст
    short_element = min(elements, key=len) #cортировка по длине элемента
    long_element = max(elements, key=len)
    print(f"Самый короткий элемент: {short_element}")
    print(f"Cамый длинный элемент: {long_element}")
else:
    print("Cписок пуст")