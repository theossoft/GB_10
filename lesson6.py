# Задача 1. Нахождение простого числа рекурсией.
# def is_prime(n, divisor=2):
#     if n == 1:
#         return False
#     elif n == 2 or n == divisor:
#         return True
#     elif n % divisor == 0:
#         return False
#     elif divisor * divisor > n:
#         return True
#     else:
#         return is_prime(n, divisor + 1)
#
# print(is_prime(3))

# Задача 2. Определить является ли предложение палиндромом
def is_palindrom(string):
    if len(string) < 2:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrom(string[1:-1].replace(" ", ""))

print(is_palindrom(input("Введите строку: ")))
