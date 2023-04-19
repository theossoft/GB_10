import random
import time

some_str = 'hello'
# Первый способ
for letter in some_str:
    print(letter)
print("--------------------------")
# Второй способ
for ind in range(0, len(some_str)):
    print(some_str[ind])
print("--------------------------")
# Посмотреть 0 символ
print(some_str[0])
print("--------------------------")
# Посмотреть последний символ в строке
print(some_str[-1])
print("--------------------------")
# Срезы. Вывести с 1 символа до 4 (не включая)
print(some_str[1:4])
print("--------------------------")
# Срезы - аналогия range(). Вывести с 1 символа до 4 (не включая), через 1 символ
print(some_str[1:4:2])
print("--------------------------")
# Срезы. Вывести от 2 индекса и до конца
print(some_str[2:])
print("--------------------------")
# Срезы. Вывести от 0 индекса и до 3
print(some_str[:3])
print("--------------------------")
# Срезы. Вывести от 0 индекса и до последнего, т.е. вся строка
print(some_str[:])
print("--------------------------")
# Срезы. Вывести всю строку с шагом -1, т.е. строка перевернется
print(some_str[::-1])
print("--------------------------")
# Выведет range(0,10)
print(range(0,10))
print("--------------------------")
# Если поставить *, то распакует значения
print(*range(0,10))
print("--------------------------")
# Списки. Индексация как в строках
some_list = [1, 'fds', True, [1, 2, 3], {1: 2}, (5, 7)]
print(some_list)
print("--------------------------")
# Списки. Заполнить список
for _ in range(10):
    # number = int(input())
    number = random.randint(1, 10)
    some_list.append(number) # Метод добавляет значения
print(some_list)
print("--------------------------")
# Списки. Метод count(), подсчет количества, работает и со строками
print(some_list.count(7))
print("--------------------------")
# Списки. Посмотреть есть ли 7 в списке
print(7 in some_list)
print("--------------------------")
# Кортеж. a = [] - список. a = (1, ) - кортеж (класс tuple), если не поставить запятую, то получится просто число
a = [1, 2, 3]
b = tuple(a) # a превращается в кортеж, ничего нельзя менять
print("--------------------------")
# Множество (set). a = {1, 2, 3}, при этом a = {} это словарь (dict), a = set() - пустое множество
print("--------------------------")
# Поиск во множестве и в списке
some_list = [random.randint(1, 10000) for i in range(10 ** 5)]
some_set = set(some_list)
start = time.perf_counter() # текущее время
print(9999 in some_list)
end = time.perf_counter()
duration1 = end-start
start = time.perf_counter()
print(9999 in some_set)
end = time.perf_counter()
duration2 = end-start
print(duration1 / duration2)
# Множество гораздо быстрее
print("--------------------------")
# Словари
some_dict = {'яблоко': 'apple', 'апельсин': 'orange'}
print(some_dict['яблоко'])
print(some_dict.get('груша', 'такого ключа нет')) # груши нет, выведет None, если get не писать, то будет ошибка. Вторым параметном можно изменить умолчание
some_dict['виноград'] = 'grape'
print(some_dict)
print("--------------------------")
# Неизменяемые str, int, float, bool, tuple, frozenset
a = 'hello'
print(id(a))
a = a + ' world'
print(id(a))
print(a)
print("--------------------------")
# Изменяемые list, set, dict