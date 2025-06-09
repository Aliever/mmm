import random

size = int(input("Введите размер массива: "))
result = []

for i in range(size):
    number = random.randint(0, 50) * 2
    result.append(number)

result.sort()

print("Массив из чётных чисел:", result)