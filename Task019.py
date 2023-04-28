# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.
import random
K = int(input("Введите число на которое будем сдвигать последовательность: "))
some_list = [random.randint(1, 10) for i in range(1, 10)]
print(some_list)

# print("Первый вариант через временный список")
# K = K % len(some_list)
# temp = []
# for i in range(0, len(some_list)):
#     temp.append(some_list[i - K])
# print(temp)

print("Второй вариант с использованием срезов")
K = K % len(some_list)
some_list[:] = some_list[-K:] + some_list[:-K]
print(some_list)