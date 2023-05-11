# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12
# (каждое число вводится с новой строки)

# Мой вариант
arr1 = [3, 1, 3, 4, 2, 4, 12]
arr2 = [4, 15, 43, 1, 15, 1]
string = str()

for i in range(0, len(arr1)):
    for j in range(0, len(arr2)):
        if arr1[i] == arr2[j]:
            break
        if arr1[i] != arr2[-1]:
            string = string + " " + str(arr1[i])
            break
print(string)

# Не мой вариант
use_list1 = int(input("Введите размер первого массива: "))
list_one = [int(input(f"{i+1} number = ")) for i in range (use_list1)]
use_list2 = int(input("Введите размер второго массива: "))
list_two = [int(input(f"{i+1} number = ")) for i in range(use_list2)]
print(*list_one)
list_two = set(list_two)
print(*list_two)
temp_list = [i for i in list_one if not i in list_two]
print(*temp_list)