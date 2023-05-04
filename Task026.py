# Задача 26:  Напишите программу,
# которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def power_recursive(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power_recursive(a, b / 2) ** 2
    else:
        return a * power_recursive(a, b - 1)

print(power_recursive(3,4))
