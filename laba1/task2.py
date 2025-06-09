def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0] #нужно чтобы поменять местами первый и последний элемент
    return lst
my_list = [1, 2, 3, 4, 5]
print(change(my_list))