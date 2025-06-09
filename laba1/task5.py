def sieve(numbers):
    uniq_nums = set(numbers) #получаем уникальные элементы преобразуя список во множество
    uniq_nums_list = list(uniq_nums) [:: -1] #переводим множество в список, и переворачиваем его
    result_tuple = tuple(uniq_nums_list) #список переводим в кортеж
    return result_tuple

input_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sieve(input_nums)
print(result)