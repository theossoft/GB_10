# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
N = abs(int(input("Введите количество оценок Василия: ")))
some_list = []
for i in range(0, N):
    some_list.append(abs(int(input(f"Введите {i+1} число: "))))
print(some_list)
for i in range(0, N):
    if some_list[i] == 5:
        some_list[i] = 1
    if some_list[i] == 4:
        some_list[i] = 2
print(some_list)