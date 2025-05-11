a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
def more(a, b):
    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print("Числа равны")
more(a, b)