# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

x = []
def fibonacci(n):
    if n in (0,1):
        x.append(1)
        return 1
    else:
        r = fibonacci(n-2) + fibonacci(n-1)
        x.append(r)
        return r

n = 8
fibonacci(n)
fibonacci(n)
print(x[-(n+1):])
