n = int(input("Введите число N: "))

total = 0
for i in range(1, n + 1):
    total += i

print("Сумма чисел от 1 до", n, "равна:", total)