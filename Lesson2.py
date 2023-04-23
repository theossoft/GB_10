# Цикл while
# summa = 0
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     if a % 2 == 0:
#         summa += a
# print(summa)

# Цикл while-else
# a = [1, 2, 3, 4, -5]
# ind = 0
# while ind < len(a):
#     if a[ind] < 0:
#         print('YES')
#         break
#     ind += 1
# else:
#     print('NO')

# Значение переменной-итератора используется
# for i in range(1, 11):
#     print(1 ** 2)

# Значение переменной-итератора не используется. Вместо i можно написать нижнее подчеркивание (_)
# for _ in range(0, 5):
#     print('HELLO')

# Варианты вывода списка
# some_list = [-3, 4, 5, 0, 1]
# for el in some_list:
#     print(el)
#
# for ind in range(0, len(some_list)):
#     print(some_list[ind])

# range 1. От, 2. До (не включая), 3. Шаг
# for i in range(100, 90, -2) # В обратную сторону
#     print(i)