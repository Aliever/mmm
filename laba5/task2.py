arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

# Сумма положительных чисел
positive_sum = 0
for num in arr:
    if num > 0:
        positive_sum += num

# Поиск индексов мин и макс
min_index = 0
max_index = 0
for i in range(len(arr)):
    if arr[i] < arr[min_index]:
        min_index = i
    if arr[i] > arr[max_index]:
        max_index = i

# Произведение между min и max
start = min(min_index, max_index) + 1
end = max(min_index, max_index)
product = 1
for i in range(start, end):
    product *= arr[i]

print("Сумма положительных чисел:", positive_sum)
print("Произведение между мин и макс:", product)