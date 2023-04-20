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

N = int(input("Введите количество элементов в списке: "))
some_list = []
for i in range(0, N):
    some_list.append(float(input(f"Введите {i+1} число: ")))
x = int(input("Введите искомое число: "))

max_element = abs(x - some_list[0])
count = 0
for i in range(1, N):
    if x > some_list[i]:
        count = abs(x - some_list[i])
        if count > max_element:
            max_element = count

print(int(max_element))


