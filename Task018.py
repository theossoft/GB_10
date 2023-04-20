# Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
#
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

N = abs(int(input("Введите количество элементов в списке: ")))
some_list = []
for i in range(0, N):
    some_list.append(abs(float(input(f"Введите {i+1} число: "))))
x = abs(float(input("Введите искомое число: ")))

count = float(0.0)
max_element = 0

for el in range(0, len(some_list)):
    if x > some_list[el] and (some_list[el] / x) > count:
        count = (some_list[el] / x)
        max_element = some_list[el]
    elif x < some_list[el] and (x / some_list[el]) > count:
        count = (x / some_list[el])
        max_element = some_list[el]

print(int(max_element))