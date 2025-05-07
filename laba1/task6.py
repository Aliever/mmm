def season_events(number_of_months):
    if number_of_months < 1 or number_of_months > 12:
        print("Введите номер месяца от 1 до 12")
        return #Завершаем выполнение функции если номер месяца некорректен


    month = {
        1: "Январе",
        2: "Феврале",
        3: "Марте",
        4: "Апреле",
        5: "Мае",
        6: "Июне",
        7: "Июле",
        8: "Августе",
        9: "Cентябре",
        10: "Октябре",
        11: "Ноябре",
        12: "Декабре"
    }
    if number_of_months in [12, 1, 2]:
        but = "За окном падал белый снег"
    elif number_of_months in [3, 4, 5]:
        but = "Птицы пели прекрасные песни"
    elif number_of_months in [6, 7, 8]:
        but = "Солнце светило ярче чем когда-либо"
    elif number_of_months in [9, 10, 11]:
        but = "Урожай был невероятным"

    name = month[number_of_months]
    print(f"Вы родились в {name}. {but}")

number_of_month = int(input("Введите номер месяца от 1 до 12: "))
season_events(number_of_month)