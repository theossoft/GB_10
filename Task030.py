# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

firstNumber = int(input("Введите первый элемент: "))
varianceNumber = int(input("Введите разность: "))
countNumber = int(input("Введите количество элементов: "))
array = [firstNumber]
for i in range(0, countNumber-1):
    array.append(array[i] + varianceNumber)
print(array)

