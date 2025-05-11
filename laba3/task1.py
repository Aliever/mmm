import datetime #Библиотека для работы с датой и временем
date = datetime.date.today() #Получаем текущую дату
a = (date.strftime("%A")) #strftime форматирует дату в строку, %A - полное название дня недели
b = (date.strftime("%B")) # %B для полного названия месяца
print(f"{a}\n{b}\nЭмиль")