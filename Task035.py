# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def simpleNumber(number):
    if number == 1:
        return "NO"
    for i in range(2, number):
        if number % i == 0:
            return "NO"
    return "YES"

print(simpleNumber(3))