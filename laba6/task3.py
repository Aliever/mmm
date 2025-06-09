class Task:
    def __init__(self, date_start, date_finish, description):
        self.date_start = date_start
        self.date_finish = date_finish
        self.description = description

# Создаем задачи с датами в формате строк
tasks = [
    Task("2025-06-01", "2025-06-05", "Задание 1"),
    Task("2025-06-02", "2025-06-09", "Задание 2"),
    Task("2025-06-03", "2025-06-08", "Задание 3"),
    Task("2025-06-04", "2025-06-09", "Задание 4"),
    Task("2025-06-05", "2025-06-07", "Задание 5")
]

# Начинаем с первого задания как с "максимального"
latest_task = tasks[0]

# Сравниваем даты как строки год-месяц-день
for task in tasks:
    if task.date_finish > latest_task.date_finish:
        latest_task = task


print("Задание с самой поздней датой окончания:", latest_task.description)
print("Дата окончания:", latest_task.date_finish)