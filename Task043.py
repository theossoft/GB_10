# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках.
# Ввод:
# 1 2 3 2 3
# Вывод:
# 2
import random

some_array = [1, 2, 3, 2, 3, 3, 3]
count_dict = {}
count = 0
for number in some_array:
    if number not in count_dict:
        count_dict[number] = 1
    else:
        count_dict[number] = count_dict[number] + 1
        if count_dict[number] == 2:
            count += 1
            count_dict[number] = 0

print(count)