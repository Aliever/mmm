a = int(input("Введите число а:"))
b = int(input("Введите число b:"))
def divide(a, b):
    if b % a == 0:
        print("true")
    else:
        print("false")
divide(a, b)