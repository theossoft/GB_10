# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
import time
from random import randint

N = int(input("Введите количество кустов на грядке: "))

blueberries = [randint(1, 100) for i in range(0, N)]
start = time.perf_counter()
sum = 0
temp_list = []
print(blueberries)

for i in range(len(blueberries)):
    if (blueberries[i] + blueberries[i - 1] + blueberries[i - 2]) > sum:
            sum = (blueberries[i] + blueberries[i - 1] + blueberries[i - 2])
            temp_list = [blueberries[i - 2], blueberries[i - 1], blueberries[i]]
end = time.perf_counter()
duration1 = end-start
print(f"Максимальное число ягод = {sum}")
print(f"Количество ягод на кустах = {temp_list}")

print("------ Эталонное решение ------")
start = time.perf_counter()
arr_count = list()
for i in range(len(blueberries) - 1):
    arr_count.append(blueberries[i - 1] + blueberries[i] + blueberries[i + 1])
arr_count.append(blueberries[-2] + blueberries[-1] + blueberries[0])
end = time.perf_counter()
duration2 = end-start
print(max(arr_count))
print(arr_count)

print(duration2 / duration1)
print(duration1 / duration2)
