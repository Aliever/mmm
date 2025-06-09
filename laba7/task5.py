
class Fitness:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

# Список из 10 занятий
sessions = [
    Fitness("C001", 2023, 1, 60),
    Fitness("C002", 2023, 2, 50),
    Fitness("C003", 2024, 3, 70),
    Fitness("C004", 2024, 4, 60),
    Fitness("C005", 2024, 5, 40),
    Fitness("C006", 2025, 6, 90),
    Fitness("C007", 2025, 7, 30),
    Fitness("C008", 2025, 8, 80),
    Fitness("C009", 2023, 9, 100),
    Fitness("C010", 2025, 10, 50)
]

# Подсчёт суммарной продолжительности занятий по каждому году
year_totals = {}  # словарь пара год-сумма минут

for session in sessions:
    if session.year in year_totals:
        year_totals[session.year] += session.duration
    else:
        year_totals[session.year] = session.duration

# Находим наибольшую сумму минут
max_total = max(year_totals.values())

# Находим  меньший год с максимальной суммой минут
best_year = None
for year in year_totals:
    if year_totals[year] == max_total:
        if best_year is None or year < best_year:
            best_year = year


print("Год с наибольшей суммарной продолжительностью занятий:", best_year)
print("Суммарная продолжительность в этом году:", max_total, "минут")