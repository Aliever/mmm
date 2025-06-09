class Fitness:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

# Список из 5 занятий
sessions = [
    Fitness("C001", 2024, 6, 50),
    Fitness("C002", 2024, 7, 30),
    Fitness("C003", 2024, 5, 90),
    Fitness("C004", 2024, 4, 45),
    Fitness("C005", 2024, 3, 60)
]

# Сначала считаем, что первое занятие и самое длинное, и самое короткое
longest = sessions[0]
shortest = sessions[0]

# Сравниваем все занятия по длительности
for session in sessions:
    if session.duration > longest.duration:
        longest = session
    if session.duration < shortest.duration:
        shortest = session


print("Самая продолжительная треня:")
print(longest.client_code, longest.year, longest.month, longest.duration, "минуток")

print("\nСамая короткая треня:")
print(shortest.client_code, shortest.year, shortest.month, shortest.duration, "минуток")