# Задача №11. Общее обсуждение
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

A = int(input("Введите число: "))
a = 0
b = 1
c = 1
i = 3
while c < A:
    a = b
    b = c
    c = a + b
    i += 1

if (A == 0):
    print(f"Число {A} находится на месте 1")
elif (A == 1):
    print(f"Число {A} находится на местах 2 и 3")
elif (c == A):
    print(f"Число {A} находится на месте {i}")
else:
    print("-1")
