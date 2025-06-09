arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
result = []

for x in arr:
    result.append(-x)

print("Массив с противоположными знаками:", result)