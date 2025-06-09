class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

# Список пользователей
users = [
    User("user1", "pass1"),
    User("user2", "pass2"),
    User("admin", "1234"),
    User("guest", "guest"),
    User("user3", "pass3")
]

# Ввод данных пользователем
search_login = input("Введите логин: ")
search_password = input("Введите пароль: ")

# Поиск пользователя
found = False #что то типо индикатора
for user in users:
    if user.login == search_login and user.password == search_password:
        print(f"Найден пользователь: {user.login}")
        found = True
        break

if not found:
    print("Пользователь с такими данными не найден.")