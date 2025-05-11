array = []
for i in range(14):
    num = int(input("Введите числа: "))
    array.append(num)
summ = sum(array)
array.append(summ)
for num in array:
    print(num)