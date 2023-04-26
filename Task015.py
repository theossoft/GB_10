# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9
import random
import sys

N = int(input(f"Введите количество арбузов: "))

watermelons = [random.randint(1, 20) for i in range(1, N)]
print(watermelons)
maxWeight = 0
minWeight = sys.maxsize
for i in range(1, len(watermelons)):
    if watermelons[i] > minWeight:
        maxWeight = watermelons[i]
    else:
        minWeight = watermelons[i]

print(f"Арбуз для себя: {maxWeight} кг., а для тещи: {minWeight} кг.")