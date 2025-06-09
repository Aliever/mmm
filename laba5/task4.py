s = input("Введите строку: ")

if s.startswith("abc"): #проверка на начало строки с abc
    s = "www" + s.removeprefix("abc") #removeprefix удаляет префикс из начала строки при его наличии
else:
    s = s + "zzz"

print("Результат:", s)