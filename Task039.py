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