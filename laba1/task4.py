def count_it(sequence):
    from collections import Counter

    #подсчитываем количество цифр
    count = Counter(sequence) #пееводит смтроку в словарь, где ключ - уникал значения, а значение кол-во повторений
    top_three = dict(count.most_common(3)) # most_commom  подсчитывает 3 самыъ повторяюшихся числа, дикт переводит кортеж который отправил most_common в словарь
    return top_three

sequence = "123463636347"
print(count_it(sequence))