# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

string = 'a a a b c a a d c d d'.split()
some_dict = {}
for i in string:
    if i in some_dict:
        print(f'{i}_{some_dict[i]}', end=" ")
        some_dict[i] = some_dict[i] + 1
    else:
        print(i, end=" ")
        some_dict[i] = 1

